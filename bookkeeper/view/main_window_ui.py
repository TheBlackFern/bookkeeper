"""
Main window UI class module.

"type: ignore[attr-defined]" comments are here becose or C++ nature of PySide
which erroniously doesn't see many attributes and methods PySide objects have.
"""

from PySide6.QtCore import (
    QRect,
    QSize,
    Qt,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class UIMainWindow:
    """
    Class for UI structure of the main window.
    """
    def __init__(self, main_window: QMainWindow):
        self.centralwidget = QWidget()
        self.statusbar = QStatusBar()
        self.table_widget = QTableWidget(self.centralwidget)
        self.show_categories_button = QPushButton(self.centralwidget)
        self.add_category_button = QPushButton(self.centralwidget)
        self.remove_expense_button = QPushButton(self.centralwidget)
        self.change_budget_button = QPushButton(self.centralwidget)
        self.add_expense_button = QPushButton(self.centralwidget)
        self.lable_budget_day = QLabel(self.centralwidget)
        self.lable_budget_week = QLabel(self.centralwidget)
        self.lable_budget_month = QLabel(self.centralwidget)
        self.label = QLabel(self.centralwidget)
        self.label_2 = QLabel(self.centralwidget)
        self.label_3 = QLabel(self.centralwidget)

        main_window.resize(530, 798)
        self.centralwidget.setObjectName("centralwidget")

        if self.table_widget.columnCount() < 4:
            self.table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()

        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget.setObjectName("tableWidget")
        self.table_widget.setGeometry(QRect(10, 50, 511, 601))
        self.table_widget.setMinimumSize(QSize(450, 351))
        self.table_widget.setAutoFillBackground(False)
        self.table_widget.setStyleSheet("")
        self.table_widget.setGridStyle(Qt.SolidLine)  # type: ignore[attr-defined]
        self.table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget.horizontalHeader().setDefaultSectionSize(90)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.verticalHeader().setVisible(False)
        self.add_category_button.setObjectName("addCategoryButton")
        self.add_category_button.setGeometry(QRect(250, 10, 151, 31))
        size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed  # type: ignore[attr-defined]
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.add_category_button.sizePolicy().hasHeightForWidth()
        )
        self.add_category_button.setSizePolicy(size_policy)
        self.add_category_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.add_category_button.setIconSize(QSize(10, 20))
        self.add_category_button.setAutoDefault(False)
        self.show_categories_button.setObjectName("showCategoriesButton")
        self.show_categories_button.setGeometry(QRect(410, 10, 111, 31))
        size_policy.setHeightForWidth(
            self.show_categories_button.sizePolicy().hasHeightForWidth()
        )
        self.show_categories_button.setSizePolicy(size_policy)
        self.show_categories_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.show_categories_button.setIconSize(QSize(10, 20))
        self.show_categories_button.setAutoDefault(False)
        self.remove_expense_button.setObjectName("removeExpenseButton")
        self.remove_expense_button.setGeometry(QRect(110, 10, 91, 31))
        size_policy.setHeightForWidth(
            self.remove_expense_button.sizePolicy().hasHeightForWidth()
        )
        self.remove_expense_button.setSizePolicy(size_policy)
        self.remove_expense_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.remove_expense_button.setIconSize(QSize(10, 20))
        self.remove_expense_button.setAutoDefault(False)
        self.change_budget_button.setObjectName("changeBudgetButton")
        self.change_budget_button.setGeometry(QRect(380, 700, 141, 31))
        size_policy.setHeightForWidth(
            self.change_budget_button.sizePolicy().hasHeightForWidth()
        )
        self.change_budget_button.setSizePolicy(size_policy)
        self.change_budget_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.change_budget_button.setIconSize(QSize(10, 20))
        self.lable_budget_day.setObjectName("lableBudgetDay")
        self.lable_budget_day.setGeometry(QRect(90, 660, 271, 31))
        self.lable_budget_day.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lable_budget_day.setAlignment(Qt.AlignCenter)  # type: ignore[attr-defined]
        self.add_expense_button.setObjectName("addExpenseButton")
        self.add_expense_button.setGeometry(QRect(10, 10, 91, 31))
        size_policy.setHeightForWidth(
            self.add_expense_button.sizePolicy().hasHeightForWidth()
        )
        self.add_expense_button.setSizePolicy(size_policy)
        self.add_expense_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.add_expense_button.setIconSize(QSize(10, 20))
        self.add_expense_button.setAutoDefault(False)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 660, 71, 31))
        self.label.setStyleSheet("font: 11pt")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 700, 71, 31))
        self.label_2.setStyleSheet("font: 11pt")
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.lable_budget_week.setObjectName("lableBudgetWeek")
        self.lable_budget_week.setGeometry(QRect(90, 700, 271, 31))
        self.lable_budget_week.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lable_budget_week.setAlignment(Qt.AlignCenter)  # type: ignore[attr-defined]
        self.lable_budget_month.setObjectName("lableBudgetMonth")
        self.lable_budget_month.setGeometry(QRect(90, 740, 271, 31))
        self.lable_budget_month.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lable_budget_month.setAlignment(Qt.AlignCenter)  # type: ignore[attr-defined]
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 740, 71, 31))
        self.label_3.setStyleSheet("font: 11pt")
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        main_window.setWindowTitle("Бухгалтер, милый мой бухгалтер")
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("Дата")
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("Сумма")
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText("Категория")
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText("Комментарий")
        self.add_expense_button.setText("Добавить")
        self.remove_expense_button.setText("Удалить")
        self.add_category_button.setText("Новая категория")
        self.show_categories_button.setText("Категории...")
        self.change_budget_button.setText("Бюджет")

        self.lable_budget_day.setText("...")
        self.lable_budget_week.setText("...")
        self.lable_budget_month.setText("...")
        self.label.setText("День")
        self.label_2.setText("Неделя")
        self.label_3.setText("Месяц")
