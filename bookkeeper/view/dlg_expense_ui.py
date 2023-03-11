# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_expense.ui'
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
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Dialog_Expense(QDialog):
    def __init__(self):
        super().__init__()
        self.gridLayoutWidget = QWidget()
        self.buttonBox = QDialogButtonBox()
        self.setDateLine = QLineEdit(self.gridLayoutWidget)
        self.setSumLine = QLineEdit(self.gridLayoutWidget)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.selectCategoryBox = QComboBox(self.gridLayoutWidget)
        self.setCommentLine = QLineEdit(self.gridLayoutWidget)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.pushButton = QPushButton()
        self.resize(515, 258)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QRect(170, 220, 193, 28))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 201))
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3.setObjectName("label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.setSumLine.setObjectName("setSumLine")
        self.setSumLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setSumLine, 1, 2, 1, 1)

        self.selectCategoryBox.setObjectName("selectCategoryBox")

        self.gridLayout.addWidget(self.selectCategoryBox, 2, 2, 1, 1)

        self.setCommentLine.setObjectName("setCommentLine")

        self.gridLayout.addWidget(self.setCommentLine, 3, 2, 1, 1)

        self.label_6.setObjectName("label_6")
        self.label_6.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5.setObjectName("label_5")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.setDateLine.setObjectName("setDateLine")
        self.setDateLine.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.setDateLine, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(468, 116, 35, 35))
        self.pushButton.setBaseSize(QSize(10, 20))
        self.pushButton.setAutoDefault(True)
        self.setLayout(self.gridLayout)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog_Expense", "\u0414\u0430\u0442\u0430", None
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "Dialog_Expense", "\u0421\u0443\u043c\u043c\u0430", None
            )
        )
        self.setDateLine.setPlaceholderText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414",
                None,
            )
        )
        self.pushButton.setText(QCoreApplication.translate("Dialog_Expense", "+", None))
