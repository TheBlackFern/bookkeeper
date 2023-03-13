"""
Pop up for displaying categories class module.
"""

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QTreeWidget,
)


class Dialog_Categories(QDialog):
    """
    Class for a pop up for displaying the categories.
    Has a title line, a tree widget and a remove category button.
    """

    def __init__(self):
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
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Список категорий")
        self.verticalLayout.addWidget(self.label)

        self.treeWidget = QTreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setGeometry(QRect(0, 40, 481, 521))
        self.treeWidget.setHeaderHidden(True)

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
