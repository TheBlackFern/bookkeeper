import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QTableWidgetItem,
)

from bookkeeper.view.main_window_ui import Ui_MainWindow
from bookkeeper.view.dlg_budget_ui import Ui_Dialog_Budget
from bookkeeper.view.dlg_categories_ui import Ui_Dialog_Categories
from bookkeeper.view.dlg_category_ui import Ui_Dialog_Category
from bookkeeper.view.dlg_expense_ui import Dialog_Expense

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


class BudgetDlg(QDialog, Ui_Dialog_Budget):
    def __init__(self):
        super(BudgetDlg, self).__init__()


class CategoriesDlg(QDialog, Ui_Dialog_Categories):
    def __init__(self):
        super(CategoriesDlg, self).__init__()


class CategoryDlg(QDialog, Ui_Dialog_Category):
    def __init__(self):
        super(CategoryDlg, self).__init__()


# class ExpenseDlg(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Dialog_Expense()
#         self.ui.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data: list[list[str, str, str, str]] | None):
        super().__init__()
        self.setupUi(self)
        self._data = data if data else []
        self.load_data()
        self.addExpenseButton.clicked.connect(self.on_add_expense_clicked)
        self.addCategoryButton.clicked.connect(self.on_add_category_clicked)
        self.changeBudgetButton.clicked.connect(self.on_change_budget_clicked)
        self.showCategoriesButton.clicked.connect(self.on_show_categories_clicked)
        self.removeExpenseButton.clicked.connect(self.on_remove_expense_clicked)

    def on_remove_expense_clicked(self):
        selected = self.tableWidget.currentRow()
        if selected != -1:
            self.tableWidget.removeRow(selected)

    def on_show_categories_clicked(self):
        ...

    def on_change_budget_clicked(self):
        ...

    def on_add_category_clicked(self):
        ...

    def on_add_expense_clicked(self):
        dialog = Dialog_Expense()
        date_input = dialog.setDateLine
        sum_input = dialog.setSumLine
        category_input = dialog.selectCategoryBox
        comment_input = dialog.setCommentLine
        dialog.buttonBox.accepted.connect(
            lambda: self.load_data(
                [
                    date_input.text(),
                    sum_input.text(),
                    category_input.currentText(),
                    comment_input.text(),
                ]
            )
        )
        dialog.show()
        dialog.exec()

    def load_data(self, expense=None):
        if expense:
            self._data = [expense] + self._data
        self.tableWidget.setRowCount(len(self._data))
        for row_num, row in enumerate(self._data):
            self.tableWidget.setItem(row_num, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(row_num, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(row_num, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(row_num, 3, QTableWidgetItem(row[3]))
        self.update()


data = [
    row.strip().split("|")
    for row in """
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(data)
    window.show()
    app.exec()
