# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_category.ui'
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
    QSizePolicy, QWidget)

class Ui_Dialog_Category(object):
    def setupUi(self, Dialog_Category):
        if not Dialog_Category.objectName():
            Dialog_Category.setObjectName(u"Dialog_Category")
        Dialog_Category.resize(518, 171)
        self.gridLayout = QGridLayout(Dialog_Category)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Dialog_Category)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.setSumLine = QLineEdit(Dialog_Category)
        self.setSumLine.setObjectName(u"setSumLine")
        self.setSumLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.gridLayout.addWidget(self.setSumLine, 0, 1, 1, 1)

        self.label_5 = QLabel(Dialog_Category)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.selectCategoryBox = QComboBox(Dialog_Category)
        self.selectCategoryBox.setObjectName(u"selectCategoryBox")

        self.gridLayout.addWidget(self.selectCategoryBox, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog_Category)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(Dialog_Category)
        self.buttonBox.accepted.connect(Dialog_Category.accept)
        self.buttonBox.rejected.connect(Dialog_Category.reject)

        QMetaObject.connectSlotsByName(Dialog_Category)
    # setupUi

    def retranslateUi(self, Dialog_Category):
        Dialog_Category.setWindowTitle(QCoreApplication.translate("Dialog_Category", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Category", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_Category", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f<br>\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
    # retranslateUi

