"""
Main window UI class module.
"""

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(530, 798)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)

        if self.tableWidget.columnCount() < 4:
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 511, 601))
        self.tableWidget.setMinimumSize(QSize(450, 351))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.addCategoryButton = QPushButton(self.centralwidget)
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.addCategoryButton.setGeometry(QRect(250, 10, 151, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.addCategoryButton.sizePolicy().hasHeightForWidth()
        )
        self.addCategoryButton.setSizePolicy(sizePolicy)
        self.addCategoryButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.addCategoryButton.setIconSize(QSize(10, 20))
        self.addCategoryButton.setAutoDefault(False)
        self.showCategoriesButton = QPushButton(self.centralwidget)
        self.showCategoriesButton.setObjectName("showCategoriesButton")
        self.showCategoriesButton.setGeometry(QRect(410, 10, 111, 31))
        sizePolicy.setHeightForWidth(
            self.showCategoriesButton.sizePolicy().hasHeightForWidth()
        )
        self.showCategoriesButton.setSizePolicy(sizePolicy)
        self.showCategoriesButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.showCategoriesButton.setIconSize(QSize(10, 20))
        self.showCategoriesButton.setAutoDefault(False)
        self.removeExpenseButton = QPushButton(self.centralwidget)
        self.removeExpenseButton.setObjectName("removeExpenseButton")
        self.removeExpenseButton.setGeometry(QRect(110, 10, 91, 31))
        sizePolicy.setHeightForWidth(
            self.removeExpenseButton.sizePolicy().hasHeightForWidth()
        )
        self.removeExpenseButton.setSizePolicy(sizePolicy)
        self.removeExpenseButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.removeExpenseButton.setIconSize(QSize(10, 20))
        self.removeExpenseButton.setAutoDefault(False)
        self.changeBudgetButton = QPushButton(self.centralwidget)
        self.changeBudgetButton.setObjectName("changeBudgetButton")
        self.changeBudgetButton.setGeometry(QRect(380, 700, 141, 31))
        sizePolicy.setHeightForWidth(
            self.changeBudgetButton.sizePolicy().hasHeightForWidth()
        )
        self.changeBudgetButton.setSizePolicy(sizePolicy)
        self.changeBudgetButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.changeBudgetButton.setIconSize(QSize(10, 20))
        self.lableBudgetDay = QLabel(self.centralwidget)
        self.lableBudgetDay.setObjectName("lableBudgetDay")
        self.lableBudgetDay.setGeometry(QRect(90, 660, 271, 31))
        self.lableBudgetDay.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lableBudgetDay.setAlignment(Qt.AlignCenter)
        self.addExpenseButton = QPushButton(self.centralwidget)
        self.addExpenseButton.setObjectName("addExpenseButton")
        self.addExpenseButton.setGeometry(QRect(10, 10, 91, 31))
        sizePolicy.setHeightForWidth(
            self.addExpenseButton.sizePolicy().hasHeightForWidth()
        )
        self.addExpenseButton.setSizePolicy(sizePolicy)
        self.addExpenseButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.addExpenseButton.setIconSize(QSize(10, 20))
        self.addExpenseButton.setAutoDefault(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 660, 71, 31))
        self.label.setStyleSheet("font: 11pt")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 700, 71, 31))
        self.label_2.setStyleSheet("font: 11pt")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lableBudgetWeek = QLabel(self.centralwidget)
        self.lableBudgetWeek.setObjectName("lableBudgetWeek")
        self.lableBudgetWeek.setGeometry(QRect(90, 700, 271, 31))
        self.lableBudgetWeek.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lableBudgetWeek.setAlignment(Qt.AlignCenter)
        self.lableBudgetMonth = QLabel(self.centralwidget)
        self.lableBudgetMonth.setObjectName("lableBudgetMonth")
        self.lableBudgetMonth.setGeometry(QRect(90, 740, 271, 31))
        self.lableBudgetMonth.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.lableBudgetMonth.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 740, 71, 31))
        self.label_3.setStyleSheet("font: 11pt")
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("Бухгалтер, милый мой бухгалтер")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("Дата")
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("Сумма")
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText("Категория")
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText("Комментарий")
        self.addExpenseButton.setText("Добавить")
        self.removeExpenseButton.setText("Удалить")
        self.addCategoryButton.setText("Новая категория")
        self.showCategoriesButton.setText("Категории...")
        self.changeBudgetButton.setText("Бюджет")

        self.lableBudgetDay.setText("...")
        self.lableBudgetWeek.setText("...")
        self.lableBudgetMonth.setText("...")
        self.label.setText("День")
        self.label_2.setText("Неделя")
        self.label_3.setText("Месяц")
