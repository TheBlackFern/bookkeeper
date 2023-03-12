import sys
import datetime
from typing import Iterable
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QTableWidgetItem,
    QMessageBox,
)

from bookkeeper.view.main_window_ui import Ui_MainWindow
from bookkeeper.view.dlg_categories_ui import Dialog_Categories
from bookkeeper.view.dlg_budget_ui import Dialog_Budget
from bookkeeper.view.dlg_category_ui import Dialog_Category
from bookkeeper.view.dlg_expense_ui import Dialog_Expense
from bookkeeper.utils import read_tree
from bookkeeper.models.budget import Budget

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
        data: list[list[str, str, str, str]] | None,
        cats: Iterable[str] | None,
        budgets: list[Budget],
    ):
        super().__init__()
        self.setupUi(self)
        self._cats = read_tree(cats) if cats else []
        self._data = data if data else []
        self._bugdet_day = budgets[0]
        self._bugdet_week = budgets[1]
        self._bugdet_month = budgets[2]
        self.load_data()
        self.update_budget()

        self.addExpenseButton.clicked.connect(self.on_add_expense_clicked)
        self.addCategoryButton.clicked.connect(self.on_add_category_clicked)
        self.changeBudgetButton.clicked.connect(self.on_change_budget_clicked)
        self.showCategoriesButton.clicked.connect(self.on_show_categories_clicked)
        self.removeExpenseButton.clicked.connect(self.on_remove_expense_clicked)

    def on_show_categories_clicked(self):
        dialog = Dialog_Categories(self._cats)
        dialog.removeCategoryButton.clicked.connect(
            lambda: self.on_remove_category_clicked(dialog)
        )
        dialog.exec()

    def on_remove_category_clicked(self, dialog):
        selected_item = dialog.treeWidget.currentItem()
        if selected_item:
            parent_item = selected_item.parent()
            if parent_item is not None:
                parent_item.removeChild(selected_item)
            else:
                index = dialog.treeWidget.indexOfTopLevelItem(selected_item)
                dialog.treeWidget.takeTopLevelItem(index)

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

    def change_budget(self, dialog, day: str, week: str, month: str):
        day_sum = float(day) if day else self._bugdet_day.amount
        week_sum = float(week) if week else self._bugdet_week.amount
        month_sum = float(month) if month else self._bugdet_month.amount
        try:
            assert day_sum >= 0
            assert week_sum >= 0
            assert month_sum >= 0
        except (ValueError, AssertionError):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Бюджет не может быть отрицательным!")
            msg.setWindowTitle("Ошибка")
            msg.exec()
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
            date_str = self.tableWidget.item(row, 0).text()
            cost_str = self.tableWidget.item(row, 1).text()
            cost_val = float(cost_str)
            date_val = datetime.date.fromisoformat(date_str)

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
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Категория с таким именем уже существует!")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            dialog.reject()
            return
        actual_parent = parent_category if parent_category != "-" else None
        self._cats.append((name, actual_parent))
        self.update()
        dialog.accept()

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

    def on_add_expense_clicked(self):
        dialog = Dialog_Expense(self._cats)
        dialog.buttonBox.accepted.connect(
            lambda: self.load_data(
                [
                    dialog.setDateLine.text(),
                    dialog.setSumLine.text(),
                    dialog.selectCategoryBox.currentText(),
                    dialog.setCommentLine.text(),
                ]
            )
        )
        dialog.exec()

    # def on_add_category_from_expense_clicked(self):
    #     self.dlg_expense.hide()
    #     self.dlg_category_from_expense.show()

    # def add_category_from_expense(self, name: str, parent_category: str):
    #     actual_parent = parent_category if parent_category != "-" else None
    #     self._cats.append((name, actual_parent))
    #     self.on_add_expense_clicked()
    #     self.update()

    def on_remove_expense_clicked(self):
        selected = self.tableWidget.currentRow()
        if selected != -1:
            self.tableWidget.removeRow(selected)

    def load_data(self, expense=None):
        if expense:
            self._data = [expense] + self._data
        self.tableWidget.setRowCount(len(self._data))
        for row_num, row in enumerate(self._data):
            self.tableWidget.setItem(row_num, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(row_num, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(row_num, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(row_num, 3, QTableWidgetItem(row[3]))
        self.update_budget()
        self.update()


if __name__ == "__main__":
    cats = """
    продукты
        хлеб
        молочные
            молоко
            кефир
            сыр
            сметана
        мясо
            сырое мясо
            мясные продукты
        сладости
        рыба
        фрукты
        овощи
        крупы
        макароны
    хозтовары
    книги
    одежда
    телефон
    """.splitlines()

    data = [
        row.strip().split("|")
        for row in """
            2023-03-12|144.99|продукты|чипсы
            2023-03-09|7.49|хозтовары|пакет на кассе
            2023-03-09|104.99|кефир|
            2023-03-09|129.99|хлеб|
            2023-03-09|239.98|сладости|пряники|
            2023-03-09|139.99|сыр|
            2023-03-09|82.99|сметана|
            2023-03-06|5536.00|книги|книги по Python и PyQt
            2023-03-05|478.00|телефон|
            2023-03-03|78.00|продукты|
            2023-03-03|1112.00|рыба|
            2023-03-03|1008.00|рыба|
            2023-03-03|156.00|рыба|
            2023-03-03|168.00|сладости|
            2023-03-03|236.73|фрукты|
            2023-03-03|16.00|хозтовары|
            2023-03-03|259.73|книги|
            2023-03-03|119.86|хлеб|
            2023-03-03|159.82|крупы|
            2023-03-03|79.91|макароны|
            2023-03-03|479.48|овощи|
        """.strip().splitlines()
    ]
    day_budget = Budget(1000.00)
    week_budget = Budget(7000.00)
    month_budget = Budget(30000.00)
    bdgts = [day_budget, week_budget, month_budget]
    app = QApplication(sys.argv)
    window = MainWindow(data, cats, bdgts)
    window.show()
    app.exec()
