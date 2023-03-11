import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QTableView,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
)
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QPalette, QColor

from bookkeeper.view.main_window_ui import Ui_MainWindow

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
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def load_data(self, data):
        self.tableWidget.setRowCount(len(data))
        for row_num, row in enumerate(data):
            self.tableWidget.setItem(row_num, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(row_num, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(row_num, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(row_num, 3, QTableWidgetItem(row[3]))


data = [
    row.strip().split("|")
    for row in """
        2023-03-09 15:09:00|7.49|хозтовары|пакет на кассе
        2023-03-09 15:09:00|104.99|кефир|
        2023-03-09 15:09:00|129.99|хлеб|
        2023-03-09 15:09:00|239.98|сладости|пряники|
        2023-03-09 15:09:00|139.99|сыр|
        2023-03-09 15:09:00|82.99|сметана|
        2023-03-06 20:32:02|5536.00|книги|книги по Python и PyQt
        2023-03-05 23:01:38|478.00|телефон|
        2023-03-03 14:18:00|78.00|продукты|
        2023-03-03 14:18:00|1112.00|рыба|
        2023-03-03 14:18:00|1008.00|рыба|
        2023-03-03 14:18:00|156.00|рыба|
        2023-03-03 14:18:00|168.00|сладости|
        2023-03-03 14:18:00|236.73|фрукты|
        2023-03-03 14:18:00|16.00|хозтовары|
        2023-03-03 13:59:00|259.73|книги|
        2023-03-03 13:59:00|119.86|хлеб|
        2023-03-03 13:59:00|159.82|крупы|
        2023-03-03 13:59:00|79.91|макароны|
        2023-03-03 13:59:00|479.48|овощи|
    """.strip().splitlines()
]

app = QApplication(sys.argv)
window = MainWindow()
window.load_data(data)
window.show()
app.exec()
