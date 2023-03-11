# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_categories.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Dialog_Categories(object):
    def setupUi(self, Dialog_Categories):
        if not Dialog_Categories.objectName():
            Dialog_Categories.setObjectName(u"Dialog_Categories")
        Dialog_Categories.resize(482, 515)
        self.treeWidget = QTreeWidget(Dialog_Categories)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 40, 481, 521))
        self.label = QLabel(Dialog_Categories)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 471, 21))
        self.label.setStyleSheet(u"background-color: rgb(255,255, 255);\n"
"font: 11pt;\n"
"border-radius: 10px")
        self.label.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_Categories)

        QMetaObject.connectSlotsByName(Dialog_Categories)
    # setupUi

    def retranslateUi(self, Dialog_Categories):
        Dialog_Categories.setWindowTitle(QCoreApplication.translate("Dialog_Categories", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_Categories", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439", None))
    # retranslateUi

