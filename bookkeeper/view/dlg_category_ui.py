# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_category.ui'
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
    QSizePolicy,
    QWidget,
)


class Dialog_Category(QDialog):
    def __init__(self, cats):
        super().__init__()
        self.setWindowTitle("Добавление категории")
        self.gridLayout = QGridLayout()
        self.setNameLine = QLineEdit()
        self.buttonBox = QDialogButtonBox()
        self.selectCategoryBox = QComboBox()
        self.label_3 = QLabel()
        self.label_5 = QLabel()

        self.resize(518, 171)

        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setObjectName("label_3")
        self.label_3.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_3.setText(
            QCoreApplication.translate(
                "Dialog_Category",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435",
                None,
            )
        )

        self.setNameLine.setObjectName("setNameLine")
        self.setNameLine.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.label_5.setObjectName("label_5")
        self.label_5.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_5.setText(
            QCoreApplication.translate(
                "Dialog_Category",
                "\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f<br>\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )

        self.selectCategoryBox.setObjectName("selectCategoryBox")
        self.selectCategoryBox.addItems(["-"] + [cat for (cat, _) in cats])

        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.setNameLine, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.selectCategoryBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.setLayout(self.gridLayout)
