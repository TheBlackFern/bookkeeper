# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_budget.ui'
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
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QWidget,
)


class Dialog_Budget(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(386, 185)
        self.setWindowTitle(
            QCoreApplication.translate("Dialog_Budget", "Установка бюджета", None)
        )

        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 0, 341, 141))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 11pt\n" "")
        self.label_4.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_4.setText(
            QCoreApplication.translate(
                "Dialog_Budget",
                "\u0411\u044e\u0434\u0436\u0435\u0442 \u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e:",
                None,
            )
        )

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.setDayBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setDayBudgetLine.setObjectName("setSumLine")
        self.setDayBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.setDayBudgetLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setDayBudgetLine, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 11pt\n" "")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog_Budget",
                "\u0411\u044e\u0434\u0436\u0435\u0442 \u043d\u0430 \u0434\u0435\u043d\u044c:",
                None,
            )
        )

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.setWeekBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setWeekBudgetLine.setObjectName("setSumLine_2")
        self.setWeekBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.setWeekBudgetLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setWeekBudgetLine, 1, 1, 1, 1)

        self.setMonthBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setMonthBudgetLine.setObjectName("setSumLine_3")
        self.setMonthBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.setMonthBudgetLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setMonthBudgetLine, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font: 11pt\n" "")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_5.setText(
            QCoreApplication.translate(
                "Dialog_Budget",
                "\u0411\u044e\u0434\u0436\u0435\u0442 \u043d\u0430 \u043c\u0435\u0441\u044f\u0446:",
                None,
            )
        )

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QRect(80, 140, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.setLayout(self.gridLayout)
