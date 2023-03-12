# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_expense.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_Expense(object):
    def setupUi(self, Dialog_Expense):
        if not Dialog_Expense.objectName():
            Dialog_Expense.setObjectName(u"Dialog_Expense")
        Dialog_Expense.resize(515, 258)
        self.buttonBox = QDialogButtonBox(Dialog_Expense)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 220, 193, 28))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.gridLayoutWidget = QWidget(Dialog_Expense)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.setSumLine = QLineEdit(self.gridLayoutWidget)
        self.setSumLine.setObjectName(u"setSumLine")
        self.setSumLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setSumLine, 1, 2, 1, 1)

        self.selectCategoryBox = QComboBox(self.gridLayoutWidget)
        self.selectCategoryBox.setObjectName(u"selectCategoryBox")

        self.gridLayout.addWidget(self.selectCategoryBox, 2, 2, 1, 1)

        self.setCommentLine = QLineEdit(self.gridLayoutWidget)
        self.setCommentLine.setObjectName(u"setCommentLine")

        self.gridLayout.addWidget(self.setCommentLine, 3, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.setDateLine = QLineEdit(self.gridLayoutWidget)
        self.setDateLine.setObjectName(u"setDateLine")
        self.setDateLine.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.setDateLine, 0, 2, 1, 1)

        self.pushButton = QPushButton(Dialog_Expense)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(468, 116, 35, 35))
        self.pushButton.setBaseSize(QSize(10, 20))
        self.pushButton.setAutoDefault(True)

        self.retranslateUi(Dialog_Expense)
        self.buttonBox.accepted.connect(Dialog_Expense.accept)
        self.buttonBox.rejected.connect(Dialog_Expense.reject)

        QMetaObject.connectSlotsByName(Dialog_Expense)
    # setupUi

    def retranslateUi(self, Dialog_Expense):
        Dialog_Expense.setWindowTitle(QCoreApplication.translate("Dialog_Expense", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Expense", u"\u0414\u0430\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_Expense", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_Expense", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_Expense", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.setDateLine.setPlaceholderText(QCoreApplication.translate("Dialog_Expense", u"\u0413\u0413\u0413\u0413-\u041c\u041c-\u0414\u0414", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_Expense", u"+", None))
    # retranslateUi

