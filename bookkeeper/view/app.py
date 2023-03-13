import sys
import datetime
from typing import Iterable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QTableWidgetItem,
    QMessageBox,
    QTreeWidgetItem,
)

from bookkeeper.view.main_window_ui import Ui_MainWindow
from bookkeeper.view.dlg_categories_ui import Dialog_Categories
from bookkeeper.view.dlg_budget_ui import Dialog_Budget
from bookkeeper.view.dlg_category_ui import Dialog_Category
from bookkeeper.view.dlg_expense_ui import Dialog_Expense
from bookkeeper.utils import read_tree
from bookkeeper.models.budget import Budget
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository

# from bookkeeper.view.expense_widget import ExpenseWidget
# from bookkeeper.view.table_widget import TableWidget

# Dialog windows for later

# class CustomDialog(QDialog):
#     self.buttonBox = QDialogButtonBox(QBtn)
#     self.buttonBox.accepted.connect(self.accept)
#     self.buttonBox.rejected.connect(self.reject)
#     self.layout = QVBoxLayout()
#     message = QLabel("Something happened, is that OK?")
#     self.layout.addWidget(message)
#     self.layout.addWidget(self.buttonBox)
#     self.setLayout(self.layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(
        self,
        data_db: SQLiteRepository[Expense],
        cats_db: SQLiteRepository[Category],
        budgets: list[Budget],
    ):
        super().__init__()
        self.setupUi(self)
        self._data_db = data_db
        self._cats_db = cats_db
        self._cats = []
        self._expenses_map_to_pk = {}
        self._cats_map_to_pk = {}
        self._cats_map_to_widget = {}
        self._pk_map_to_cats = {}
        self._pk_map_to_expenses = {}
        self._bugdet_day = budgets[0]
        self._bugdet_week = budgets[1]
        self._bugdet_month = budgets[2]
        self._last_selected_item_text = ""
        self._last_selected_category_text = ""
        self.load_data()
        self.get_cats_from_db()
        self.update_budget()

        self.addExpenseButton.clicked.connect(self.on_add_expense_clicked)
        self.addCategoryButton.clicked.connect(self.on_add_category_clicked)
        self.changeBudgetButton.clicked.connect(self.on_change_budget_clicked)
        self.showCategoriesButton.clicked.connect(self.on_show_categories_clicked)
        self.removeExpenseButton.clicked.connect(self.on_remove_expense_clicked)
        self.tableWidget.itemChanged.connect(self.on_expense_change)
        self.tableWidget.itemClicked.connect(self.on_expense_selection)

    def on_add_expense_clicked(self):
        dialog = Dialog_Expense(self._cats)
        dialog.buttonBox.accepted.connect(
            lambda: self.load_data(
                (
                    dialog.setDateLine.text(),
                    dialog.setSumLine.text(),
                    dialog.selectCategoryBox.currentText(),
                    dialog.setCommentLine.text(),
                )
            )
        )
        dialog.exec()

    def on_add_category_clicked(self):
        dialog = Dialog_Category(self._cats)
        dialog.buttonBox.accepted.connect(
            lambda: self.add_category(
                dialog,
                dialog.setNameLine.text(),
                dialog.selectCategoryBox.currentText(),
            )
        )
        dialog.exec()

    def on_change_budget_clicked(self):
        dialog = Dialog_Budget()
        dialog.buttonBox.accepted.connect(
            lambda: self.change_budget(
                dialog,
                dialog.setDayBudgetLine.text(),
                dialog.setWeekBudgetLine.text(),
                dialog.setMonthBudgetLine.text(),
            )
        )
        dialog.exec()

    def on_show_categories_clicked(self):
        dialog = Dialog_Categories()
        self.populate(dialog)
        dialog.treeWidget.itemChanged.connect(self.on_category_change)
        dialog.treeWidget.itemClicked.connect(self.on_category_selection)
        dialog.removeCategoryButton.clicked.connect(
            lambda: self.on_remove_category_clicked(dialog)
        )
        dialog.exec()

    def on_remove_expense_clicked(self):
        selected = self.tableWidget.currentRow()
        if selected != -1:
            self.tableWidget.removeRow(selected)
            self._data_db.delete(self._expenses_map_to_pk[selected])
            self.update()
            self.update_budget()

    def on_remove_category_clicked(self, dialog):
        selected_item = dialog.treeWidget.currentItem()
        if selected_item:
            parent_item = selected_item.parent()
            if parent_item is not None:
                parent_item.removeChild(selected_item)
            else:
                index = dialog.treeWidget.indexOfTopLevelItem(selected_item)
                dialog.treeWidget.takeTopLevelItem(index)

            pk = self._cats_map_to_pk[selected_item.text(0)]
            cat = self._cats_db.get(pk)
            assert cat is not None
            children = cat.get_subcategories(self._cats_db)
            for child in children:
                self._cats_db.delete(child.pk)
                related_exps = self._data_db.get_all_where({"category": child.name})
                if related_exps:
                    for exp in related_exps:
                        self._data_db.delete(exp.pk)
            related_exps = self._data_db.get_all_where({"category": cat.name})
            if related_exps:
                for exp in related_exps:
                    self._data_db.delete(exp.pk)
            self._cats_db.delete(cat.pk)
            self.get_cats_from_db()
            self.load_data()
            self.update_budget()
            self.update()

    def on_expense_change(self, item):
        if (
            not self.tableWidget.item(item.row(), 0)
            or not self.tableWidget.item(item.row(), 1)
            or not self.tableWidget.item(item.row(), 2)
            or not self.tableWidget.item(item.row(), 3)
        ):
            return  # so that there are no error when items are added in
        is_valid = True
        pk = self._expenses_map_to_pk[item.row()]
        match item.column():
            case 0:
                is_valid = self._validate_expense(date=item.text())
            case 1:
                is_valid = self._validate_expense(amount=item.text())
            case 2:
                is_valid = self._validate_expense(cat=item.text())

        if not is_valid:
            self.tableWidget.setItem(
                item.row(),
                item.column(),
                QTableWidgetItem(self._last_selected_item_text),
            )
            return
        upd_expense = Expense(
            expense_date=self.tableWidget.item(item.row(), 0).text(),
            amount=self.tableWidget.item(item.row(), 1).text(),
            category=self.tableWidget.item(item.row(), 2).text(),
            comment=self.tableWidget.item(item.row(), 3).text(),
            pk=pk,
        )
        self._data_db.update(upd_expense)
        print(item.row(), item.column(), item.text())

        self.update_budget()

    def on_expense_selection(self, item):
        if item:
            self._last_selected_item_text = item.text()
            print(self._last_selected_item_text)

    def on_category_change(self, item):
        cats = [name for (name, _) in self._cats]
        if item.text(0) in cats:
            throw_error("Категория с таким именем уже существует!")
            widget = self._cats_map_to_widget[item.text(0)]
            widget.setText(self._last_selected_category_text)
            return
        pk = self._cats_map_to_pk[self._last_selected_category_text]
        cat = self._cats_db.get(pk)
        assert cat is not None  # it cannot be under normal conditions
        related_exps = self._data_db.get_all_where({"category": cat.name})
        if related_exps:
            for exp in related_exps:
                exp.category = item.text(0)
                self._data_db.update(exp)
        cat.name = item.text(0)
        self._cats_db.update(cat)
        print(item.text(0))
        self.update()

    def on_category_selection(self, item):
        if item:
            self._last_selected_category_text = item.text(0)
            print(self._last_selected_category_text)

    def change_budget(self, dialog, day: str, week: str, month: str):
        day_sum = float(day) if day else self._bugdet_day.amount
        week_sum = float(week) if week else self._bugdet_week.amount
        month_sum = float(month) if month else self._bugdet_month.amount
        try:
            assert day_sum >= 0
            assert week_sum >= 0
            assert month_sum >= 0
        except (ValueError, AssertionError):
            throw_error("Бюджет не может быть отрицательным!")
            dialog.reject()
            return

        self._bugdet_day.amount = day_sum
        self._bugdet_week.amount = week_sum
        self._bugdet_month.amount = month_sum
        self.update_budget()
        dialog.accept()

    def set_budget_text(self, amount: float, period: str):
        budget_lables = {
            "day": (self.lableBudgetDay, self._bugdet_day),
            "week": (self.lableBudgetWeek, self._bugdet_week),
            "month": (self.lableBudgetMonth, self._bugdet_month),
        }
        current_budget_sum = budget_lables[period][1]
        current_budget_lable = budget_lables[period][0]
        current_budget_lable.setText(f"{amount:.2f} / {current_budget_sum.amount:.2f}")
        if amount > current_budget_sum.amount:
            current_budget_lable.setStyleSheet(
                "background-color: rgb(255,255, 255);\n"
                "font: 11pt;\n"
                "border-radius: 10px;\n"
                "color: rgb(255,0,0)"
            )
        else:
            current_budget_lable.setStyleSheet(
                "background-color: rgb(255,255, 255);\n"
                "font: 11pt;\n"
                "border-radius: 10px;\n"
                "color: rgb(0,0,0)"
            )

    def update_budget(self):
        today = datetime.date.today()
        today_sum = 0
        week_sum = 0
        month_sum = 0

        for row in range(self.tableWidget.rowCount()):
            if not self.tableWidget.item(row, 0) or not self.tableWidget.item(row, 1):
                continue
            date_str = self.tableWidget.item(row, 0).text()
            cost_str = self.tableWidget.item(row, 1).text()

            cost_val = float(cost_str) if cost_str else 0.0
            date_val = datetime.date.fromisoformat(date_str) if date_str else today

            if date_val == today:
                today_sum += cost_val

            if (
                date_val.isocalendar()[1] == today.isocalendar()[1]
                and date_val.year == today.year
            ):
                week_sum += cost_val

            if date_val.month == today.month and date_val.year == today.year:
                month_sum += cost_val

        self.set_budget_text(today_sum, "day")
        self.set_budget_text(week_sum, "week")
        self.set_budget_text(month_sum, "month")

    def add_category(self, dialog, name: str, parent_category: str):
        cat_names = {name for (name, _) in self._cats}
        if name in cat_names:
            throw_error("Категория с таким именем уже существует!")
            dialog.reject()
            return
        actual_parent = parent_category if parent_category != "-" else None
        self._cats.append((name, actual_parent))
        if actual_parent:
            cat_obj = Category(name=name, parent=self._cats_map_to_pk[actual_parent])
        else:
            cat_obj = Category(name=name, parent=None)
        self._cats_db.add(cat_obj)
        self.get_cats_from_db()
        self.update()
        dialog.accept()

    # def on_add_category_from_expense_clicked(self):
    #     self.dlg_expense.hide()
    #     self.dlg_category_from_expense.show()

    # def add_category_from_expense(self, name: str, parent_category: str):
    #     actual_parent = parent_category if parent_category != "-" else None
    #     self._cats.append((name, actual_parent))
    #     self.on_add_expense_clicked()
    #     self.update()

    def load_data(self, expense: tuple[str, str, str, str] | None = None):
        if expense:
            if self._validate_expense(
                date=expense[0], amount=expense[1], cat=expense[2]
            ):
                self._data_db.add(
                    Expense(
                        expense_date=expense[0],
                        amount=expense[1],
                        category=expense[2],
                        comment=expense[3],
                    )
                )

        self._expenses_map_to_pk = {}
        self._pk_map_to_expenses = {}
        if data := self._data_db.get_all_where():
            self.tableWidget.setRowCount(len(data))
            for row_num, exp in enumerate(data[::-1]):
                self._expenses_map_to_pk[row_num] = exp.pk
                self._pk_map_to_expenses[exp.pk] = row_num
                print(self._expenses_map_to_pk)
                self.tableWidget.setItem(row_num, 0, QTableWidgetItem(exp.expense_date))
                self.tableWidget.setItem(row_num, 1, QTableWidgetItem(exp.amount))
                self.tableWidget.setItem(row_num, 2, QTableWidgetItem(exp.category))
                self.tableWidget.setItem(row_num, 3, QTableWidgetItem(exp.comment))
        self.update_budget()
        self.update()

    def _validate_expense(
        self,
        date: str = datetime.date.today().strftime("%Y-%m-%d"),
        amount: str = "100",
        cat: str | None = None,
    ) -> bool:
        try:
            assert datetime.date.fromisoformat(date)
        except ValueError:
            throw_error("Неверный формат даты!")
            return False
        try:
            assert float(amount) >= 0
        except AssertionError:
            throw_error("Сумма не может быть отрицательной!")
            return False
        try:
            if cat is None:
                return True
            cat_names = [name for (name, _) in self._cats]
            assert cat in cat_names
        except AssertionError:
            throw_error("Категории не существует!")
            return False
        return True

    def get_cats_from_db(self):
        cats = self._cats_db.get_all_where()
        print(cats)
        if cats:
            self._cats_map_to_pk = {}
            self._pk_map_to_cats = {}
            for cat in cats:
                self._cats_map_to_pk[cat.name] = cat.pk
                self._pk_map_to_cats[cat.pk] = cat.name
            self._cats = []
            for cat in cats:
                if cat.parent:
                    self._cats.append((cat.name, self._pk_map_to_cats[cat.parent]))
                else:
                    self._cats.append((cat.name, None))
        self.update()

    def populate(self, dialog):
        known_parents = {}
        self._cats_map_to_widget = {}
        for (name, parent) in self._cats:
            if parent:
                parent_item = known_parents[parent]
                item = QTreeWidgetItem(parent_item, [name])
            else:
                item = QTreeWidgetItem(dialog.treeWidget, [name])
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            known_parents[name] = item
            self._cats_map_to_widget[name] = item


def throw_error(text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.setWindowTitle("Ошибка")
    msg.exec()


if __name__ == "__main__":
    # cats = """
    # продукты
    #     хлеб
    #     молочные
    #         молоко
    #         кефир
    #         сыр
    #         сметана
    #     мясо
    #         сырое мясо
    #         мясные продукты
    #     сладости
    #     рыба
    #     фрукты
    #     овощи
    #     крупы
    #     макароны
    # хозтовары
    # книги
    # одежда
    # телефон
    # """.splitlines()

    # data = [
    #     row.strip().split("|")
    #     for row in """
    #         2023-03-12|144.99|продукты|чипсы
    #         2023-03-09|7.49|хозтовары|пакет на кассе
    #         2023-03-09|104.99|кефир|
    #         2023-03-09|129.99|хлеб|
    #         2023-03-09|239.98|сладости|пряники|
    #         2023-03-09|139.99|сыр|
    #         2023-03-09|82.99|сметана|
    #         2023-03-06|5536.00|книги|книги по Python и PyQt
    #         2023-03-05|478.00|телефон|
    #         2023-03-03|78.00|продукты|
    #         2023-03-03|1112.00|рыба|
    #         2023-03-03|1008.00|рыба|
    #         2023-03-03|156.00|рыба|
    #         2023-03-03|168.00|сладости|
    #         2023-03-03|236.73|фрукты|
    #         2023-03-03|16.00|хозтовары|
    #         2023-03-03|259.73|книги|
    #         2023-03-03|119.86|хлеб|
    #         2023-03-03|159.82|крупы|
    #         2023-03-03|79.91|макароны|
    #         2023-03-03|479.48|овощи|
    #     """.strip().splitlines()
    # ]
    db_name = "databases/sql.db"
    expense_db = SQLiteRepository[Expense](db_name, Expense)
    category_db = SQLiteRepository[Category](db_name, Category)
    budget_db = SQLiteRepository[Budget](db_name, Budget)
    day_budget = Budget(1000.00)
    week_budget = Budget(7000.00)
    month_budget = Budget(30000.00)
    bdgts = [day_budget, week_budget, month_budget]
    app = QApplication(sys.argv)
    window = MainWindow(expense_db, category_db, bdgts)
    window.show()
    app.exec()
