"""
App presenter class module.

"type: ignore[attr-defined]" comments are here becose or C++ nature of PySide
which erroniously doesn't see many attributes and methods PySide objects have.
"""
import sys
import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
    QTreeWidgetItem,
)

from bookkeeper.view.main_window_ui import UIMainWindow
from bookkeeper.view.dlg_categories_ui import DialogCategories
from bookkeeper.view.dlg_budget_ui import DialogBudget
from bookkeeper.view.dlg_category_ui import DialogCategory
from bookkeeper.view.dlg_expense_ui import DialogExpense
from bookkeeper.models.budget import Budget
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository


class MainWindow(QMainWindow, UIMainWindow):
    """
    The main window of an app, also sets interaction logic for all elements
    and databases.

    The double inheretence supplies both UI and functionality of a window.
    The order is supposed to be QMainWindow, UIMainWindow, but then MRO
    would be QMainWindow -> UIMainWindow -> QWidget -> QObject -> ... But we have to call
    QMainWindow -> QWidget -> ... part and then UIMainWindow, as UI class requiers an
    existing window to style. The easiest way to solve this issue is not to call
    super().__init__() but to explicitly call classes' constructors.
    """
    def __init__(
        self,
        data_db: SQLiteRepository[Expense],
        cats_db: SQLiteRepository[Category],
        budget_db: SQLiteRepository[Budget],
    ):
        QMainWindow.__init__(self)  # now self is a QMainWindow object
        UIMainWindow.__init__(self, self)  # so we can pass it as a main_window argument
        self._data_db = data_db
        self._cats_db = cats_db
        self._budget_db = budget_db
        self._cats: list[tuple[str, str | None]] = []
        self._expenses_map_to_pk: dict[int, int] = {}
        self._cats_map_to_pk: dict[str, int] = {}
        self._cats_map_to_widget: dict[str, QTreeWidgetItem] = {}
        self._pk_map_to_cats: dict[int, str] = {}
        self._pk_map_to_expenses: dict[int, int] = {}
        self._bugdet_day = budget_db.get(1)
        self._bugdet_week = budget_db.get(2)
        self._bugdet_month = budget_db.get(3)
        self._last_selected_item_text = ""
        self._last_selected_category_text = ""
        self.populate_table()
        self.get_cats_from_db()
        self.update_budget()

        self.add_expense_button.clicked.connect(  # type: ignore[attr-defined]
            self.on_add_expense_clicked
        )
        self.add_category_button.clicked.connect(  # type: ignore[attr-defined]
            self.on_add_category_clicked
        )
        self.change_budget_button.clicked.connect(  # type: ignore[attr-defined]
            self.on_change_budget_clicked
        )
        self.show_categories_button.clicked.connect(  # type: ignore[attr-defined]
            self.on_show_categories_clicked
        )
        self.remove_expense_button.clicked.connect(  # type: ignore[attr-defined]
            self.on_remove_expense_clicked
        )
        self.table_widget.itemChanged.connect(  # type: ignore[attr-defined]
            self.on_expense_change
        )
        self.table_widget.itemClicked.connect(  # type: ignore[attr-defined]
            self.on_expense_selection
        )

    def on_add_expense_clicked(self) -> None:
        """
        Pop up a widget for adding in an expense.
        """
        dialog = DialogExpense(self._cats)
        dialog.button_box.accepted.connect(  # type: ignore[attr-defined]
            lambda: self.populate_table(
                (
                    dialog.set_date_line.text(),
                    dialog.set_sum_line.text(),
                    dialog.select_category_box.currentText(),
                    dialog.set_comment_line.text(),
                )
            )
        )
        dialog.exec()

    def on_add_category_clicked(self) -> None:
        """
        Pop up a widget for adding in a category.
        """
        dialog = DialogCategory(self._cats)
        dialog.button_box.accepted.connect(  # type: ignore[attr-defined]
            lambda: self.add_category(
                dialog,
                dialog.set_name_line.text(),
                dialog.select_category_box.currentText(),
            )
        )
        dialog.exec()

    def on_change_budget_clicked(self) -> None:
        """
        Pop up a widget for changing the budget.
        """
        dialog = DialogBudget()
        dialog.button_box.accepted.connect(  # type: ignore[attr-defined]
            lambda: self.change_budget(
                dialog,
                dialog.set_day_budget_line.text(),
                dialog.set_week_budget_line.text(),
                dialog.set_month_budget_line.text(),
            )
        )
        dialog.exec()

    def on_show_categories_clicked(self) -> None:
        """
        Pop up a widget with a categories tree.
        """
        dialog = DialogCategories()
        self.populate_tree(dialog)
        dialog.tree_widget.itemChanged.connect(  # type: ignore[attr-defined]
            self.on_category_change
        )
        dialog.tree_widget.itemClicked.connect(  # type: ignore[attr-defined]
            self.on_category_selection
        )
        dialog.remove_category_button.clicked.connect(  # type: ignore[attr-defined]
            lambda: self.on_remove_category_clicked(dialog)
        )
        dialog.exec()

    def on_remove_expense_clicked(self) -> None:
        """
        Remove an expense from a table and from database.
        """
        selected = self.table_widget.currentRow()
        if selected != -1:
            self.table_widget.removeRow(selected)
            self._data_db.delete(self._expenses_map_to_pk[selected])
            self.update()
            self.update_budget()

    def on_remove_category_clicked(self, dialog: DialogCategories) -> None:
        """
        Remove a category, all of its sub-categories, all of expenses that are
        related to all these categories and all of the respective database entries.
        An expense cannot have a None category, so removing all expenses is forced.
        """
        selected_item = dialog.tree_widget.currentItem()
        if selected_item:
            parent_item = selected_item.parent()
            if parent_item is not None:
                parent_item.removeChild(selected_item)
            else:
                index = dialog.tree_widget.indexOfTopLevelItem(selected_item)
                dialog.tree_widget.takeTopLevelItem(index)

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
            self.populate_table()
            self.update_budget()
            self.update()

    def on_expense_change(self, item: QTableWidgetItem) -> None:
        """
        Update an expense and its database entry, if it's a valid edit.
        """
        if (
            not self.table_widget.item(item.row(), 0)
            or not self.table_widget.item(item.row(), 1)
            or not self.table_widget.item(item.row(), 2)
            or not self.table_widget.item(item.row(), 3)
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
            self.table_widget.setItem(
                item.row(),
                item.column(),
                QTableWidgetItem(self._last_selected_item_text),
            )
            return
        upd_expense = Expense(
            expense_date=self.table_widget.item(item.row(), 0).text(),
            amount=self.table_widget.item(item.row(), 1).text(),
            category=self.table_widget.item(item.row(), 2).text(),
            comment=self.table_widget.item(item.row(), 3).text(),
            pk=pk,
        )
        self._data_db.update(upd_expense)
        self.update_budget()

    def on_expense_selection(self, item: QTableWidgetItem | None) -> None:
        """ "
        Constant monitoring of selected table entries, for the cases when
        the entry text is changed, but the change is flawed and we have
        to undo it (for example, when the sum was changed to a negative number).
        """
        if item:
            self._last_selected_item_text = item.text()

    def on_category_change(self, item: QTreeWidgetItem) -> None:
        """
        Update the category, it's database entry and all of the entries, if it's
        a valid edit.
        """
        if item.text(0) == self._last_selected_category_text:
            return
        cats = [name for (name, _) in self._cats]
        if item.text(0) in cats:
            throw_error("Категория с таким именем уже существует!")
            widget = self._cats_map_to_widget[self._last_selected_category_text]
            widget.setText(0, self._last_selected_category_text)
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
        self.get_cats_from_db()
        self.populate_table()
        self.update_budget()
        self.update()

    def on_category_selection(self, item: QTreeWidgetItem | None) -> None:
        """ "
        Constant monitoring of selected categories, for the cases when
        the category text is changed, but the change is flawed and we have
        to undo it (for example, when the name was changed to an already
        existing one).
        """
        if item:
            self._last_selected_category_text = item.text(0)

    def change_budget(
        self, dialog: DialogBudget, day: str, week: str, month: str
    ) -> None:
        """
        Change budget with the numbers given (in string format).
        """
        # they never are
        assert self._bugdet_day is not None
        assert self._bugdet_week is not None
        assert self._bugdet_month is not None
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
        self._budget_db.update(self._bugdet_day)
        self._budget_db.update(self._bugdet_week)
        self._budget_db.update(self._bugdet_month)
        self.update_budget()
        dialog.accept()

    def set_budget_text(self, amount: float, period: str) -> None:
        """
        Set the text inside the budget widget to display current budget status.
        It would look like " current spent / budget sum ".
        """
        # they never are
        assert self._bugdet_day is not None
        assert self._bugdet_week is not None
        assert self._bugdet_month is not None
        budget_lables = {
            "day": (self.lable_budget_day, self._bugdet_day),
            "week": (self.lable_budget_week, self._bugdet_week),
            "month": (self.lable_budget_month, self._bugdet_month),
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

    def update_budget(self) -> None:
        """
        Update all budgets for possible changes.
        """
        today = datetime.date.today()
        today_sum = 0.0
        week_sum = 0.0
        month_sum = 0.0

        for row in range(self.table_widget.rowCount()):
            if not self.table_widget.item(row, 0) or not self.table_widget.item(row, 1):
                continue
            date_str = self.table_widget.item(row, 0).text()
            cost_str = self.table_widget.item(row, 1).text()

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

    def add_category(
        self, dialog: DialogCategory, name: str, parent_category: str
    ) -> None:
        """
        Add category to the database if a category with the same name doesn't exist.
        """
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

    def _validate_expense(
        self,
        date: str = datetime.date.today().strftime("%Y-%m-%d"),
        amount: str = "100",
        cat: str | None = None,
    ) -> bool:
        """
        Check if proposed parameters are suitable for an expense.
        Date should be in YYYY-MM-DD format.
        Amount should be a non-negative real number.
        Category should be from existing categories.
        """
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

    def get_cats_from_db(self) -> None:
        """
        Get category an its heirarchy from the database.
        """
        cats = self._cats_db.get_all_where()
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

    def populate_table(self, expense: tuple[str, str, str, str] | None = None) -> None:
        """
        Populate the table widget with expenses from a database. Possibly add a new
        expense.
        """
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
            self.table_widget.setRowCount(len(data))
            for row_num, exp in enumerate(data[::-1]):
                self._expenses_map_to_pk[row_num] = exp.pk
                self._pk_map_to_expenses[exp.pk] = row_num
                self.table_widget.setItem(row_num, 0, QTableWidgetItem(exp.expense_date))
                self.table_widget.setItem(row_num, 1, QTableWidgetItem(exp.amount))
                self.table_widget.setItem(row_num, 2, QTableWidgetItem(exp.category))
                self.table_widget.setItem(row_num, 3, QTableWidgetItem(exp.comment))
        self.update_budget()
        self.update()

    def populate_tree(self, dialog: DialogCategories) -> None:
        """
        Populate the tree widget with categories from a database.
        """
        known_parents: dict[str, QTreeWidgetItem] = {}
        self._cats_map_to_widget = {}
        for name, parent in self._cats:
            if parent:
                parent_item = known_parents[parent]
                item = QTreeWidgetItem(parent_item, [name])
            else:
                item = QTreeWidgetItem(dialog.tree_widget, [name])
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # type: ignore[attr-defined]
            known_parents[name] = item
            self._cats_map_to_widget[name] = item


def throw_error(text: str) -> None:
    """
    Create an error pop with a message.
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)  # type: ignore[attr-defined]
    msg.setText(text)
    msg.setWindowTitle("Ошибка")
    msg.exec()


if __name__ == "__main__":
    DB_NAME = "databases/sql.db"
    expenses_db = SQLiteRepository[Expense](DB_NAME, Expense)
    categories_db = SQLiteRepository[Category](DB_NAME, Category)
    budgets_db = SQLiteRepository[Budget](DB_NAME, Budget)
    app = QApplication(sys.argv)
    window = MainWindow(expenses_db, categories_db, budgets_db)
    window.show()
    app.exec()
