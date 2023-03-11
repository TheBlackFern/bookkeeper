# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_budget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog_Budget(object):
    def setupUi(self, Dialog_Budget):
        if not Dialog_Budget.objectName():
            Dialog_Budget.setObjectName(u"Dialog_Budget")
        Dialog_Budget.resize(512, 135)
        self.buttonBox = QDialogButtonBox(Dialog_Budget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 90, 461, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(Dialog_Budget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 491, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.setSumLine = QLineEdit(self.widget)
        self.setSumLine.setObjectName(u"setSumLine")
        self.setSumLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.horizontalLayout.addWidget(self.setSumLine)


        self.retranslateUi(Dialog_Budget)
        self.buttonBox.accepted.connect(Dialog_Budget.accept)
        self.buttonBox.rejected.connect(Dialog_Budget.reject)

        QMetaObject.connectSlotsByName(Dialog_Budget)
    # setupUi

    def retranslateUi(self, Dialog_Budget):
        Dialog_Budget.setWindowTitle(QCoreApplication.translate("Dialog_Budget", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Budget", u"\u0411\u044e\u0434\u0436\u0435\u0442 \u043d\u0430 \u043c\u0435\u0441\u044f\u0446:", None))
    # retranslateUi

