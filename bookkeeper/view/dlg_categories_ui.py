# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_categories.ui'
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
    QDialog,
    QHeaderView,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)


class Dialog_Categories(QDialog):
    def __init__(self, cats):
        super().__init__()
        self.resize(482, 515)
        self.setWindowTitle("Список категорий")
        self.verticalLayout = QVBoxLayout()

        self.label = QLabel()
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 471, 21))
        self.label.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.label.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(
            QCoreApplication.translate(
                "Dialog_Categories",
                "\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439",
                None,
            )
        )
        self.verticalLayout.addWidget(self.label)

        self.treeWidget = QTreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setGeometry(QRect(0, 40, 481, 521))
        self.treeWidget.setHeaderHidden(True)
        self.populate(cats)

        self.verticalLayout.addWidget(self.treeWidget)

        self.removeCategoryButton = QPushButton()
        self.removeCategoryButton.setText("Удалить категорию со всеми подкатегориями")
        self.removeCategoryButton.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.verticalLayout.addWidget(self.removeCategoryButton)

        self.setLayout(self.verticalLayout)

    def populate(self, cats):
        known_parents = {}
        for (name, parent) in cats:
            if parent:
                parent_item = known_parents[parent]
                item = QTreeWidgetItem(parent_item, [name])
            else:
                item = QTreeWidgetItem(self.treeWidget, [name])
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            known_parents[name] = item
