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
    def __init__(self, cats):
        super().__init__()
        self.setWindowTitle("Добавление траты")
        self.gridLayout = QGridLayout()
        self.gridLayoutWidget = QWidget()
        self.buttonBox = QDialogButtonBox()
        self.setDateLine = QLineEdit()
        self.setSumLine = QLineEdit()
        self.selectCategoryBox = QComboBox()
        self.setCommentLine = QLineEdit()
        self.addCategoryButton = QPushButton()
        self.label_3 = QLabel()
        self.label_4 = QLabel()
        self.label_5 = QLabel()
        self.label_6 = QLabel()

        self.resize(450, 258)

        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.label_3.setObjectName("label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog_Expense", "\u0414\u0430\u0442\u0430", None
            )
        )

        self.label_4.setObjectName("label_4")
        self.label_4.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_4.setText(
            QCoreApplication.translate(
                "Dialog_Expense", "\u0421\u0443\u043c\u043c\u0430", None
            )
        )

        self.label_5.setObjectName("label_5")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_5.setText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )

        self.label_6.setObjectName("label_6")
        self.label_6.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_6.setText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            )
        )

        self.setDateLine.setObjectName("setDateLine")
        self.setDateLine.setAutoFillBackground(False)
        self.setDateLine.setPlaceholderText(
            QCoreApplication.translate(
                "Dialog_Expense",
                "\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414",
                None,
            )
        )

        self.setSumLine.setObjectName("setSumLine")
        self.setSumLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.selectCategoryBox.setObjectName("selectCategoryBox")
        self.selectCategoryBox.addItems([cat for (cat, _) in cats])

        self.setCommentLine.setObjectName("setCommentLine")

        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.setDateLine, 0, 3, 1, 8)
        self.gridLayout.addWidget(self.setSumLine, 1, 3, 1, 8)
        self.gridLayout.addWidget(self.selectCategoryBox, 2, 3, 1, 8)
        self.gridLayout.addWidget(self.setCommentLine, 3, 3, 1, 8)
        self.gridLayout.addWidget(self.buttonBox, 4, 5, 1, 4)
        # possibly have an add category button here too
        # self.addCategoryButton.setObjectName("addCategoryButton")
        # self.addCategoryButton.setEnabled(True)
        # self.addCategoryButton.setAutoDefault(True)
        # self.addCategoryButton.setText(
        #     QCoreApplication.translate("Dialog_Expense", "+", None)
        # )
        # self.addCategoryButton.setStyleSheet(
        #     "color: white;\n"
        #     "background-color: rgb(11, 121, 255);\n"
        #     "font: 13pt;\n"
        #     "border-radius: 6px"
        # )
        # self.gridLayout.addWidget(self.addCategoryButton, 2, 12, 1, 1)
        self.setLayout(self.gridLayout)
