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
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 821)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(10, 10, 651, 791))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.widget)
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
        self.tableWidget.setMinimumSize(QSize(601, 351))

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0440\u0430\u0442\u0443",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0411\u044e\u0434\u0436\u0435\u0442", None
            )
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

    # retranslateUi
