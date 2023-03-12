# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookkeeper.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 723)
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
        self.tableWidget.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
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
        self.changeBudgetButton.setGeometry(QRect(380, 660, 141, 31))
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
        self.budgetLabel = QLabel(self.centralwidget)
        self.budgetLabel.setObjectName("budgetLabel")
        self.budgetLabel.setGeometry(QRect(10, 660, 361, 31))
        self.budgetLabel.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.budgetLabel.setAlignment(Qt.AlignCenter)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Бухгалтер, милый мой бухгалтер", None)
        )
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "\u0414\u0430\u0442\u0430", None)
        )
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0421\u0443\u043c\u043c\u0430", None
            )
        )
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            )
        )
        self.addCategoryButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u043e\u0432\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )
        self.showCategoriesButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438...",
                None,
            )
        )
        self.removeExpenseButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None
            )
        )
        self.changeBudgetButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0411\u044e\u0434\u0436\u0435\u0442", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.budgetLabel.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.budgetLabel.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        self.addExpenseButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )

    # retranslateUi
