"""
Pop up for displaying categories class module.

"type: ignore[attr-defined]" comments are here becose or C++ nature of PySide
which erroniously doesn't see many attributes and methods PySide objects have.
"""

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QTreeWidget,
)


class DialogCategories(QDialog):
    """
    Class for a pop up for displaying the categories.
    Has a title line, a tree widget and a remove category button.
    """
    def __init__(self) -> None:
        super().__init__()
        self.resize(482, 515)
        self.setWindowTitle("Список категорий")
        self.vertical_layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 471, 21))
        self.label.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.label.setAlignment(Qt.AlignCenter)  # type: ignore[attr-defined]
        self.label.setText("Список категорий")
        self.vertical_layout.addWidget(self.label)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setObjectName("treeWidget")
        self.tree_widget.setGeometry(QRect(0, 40, 481, 521))
        self.tree_widget.setHeaderHidden(True)

        self.vertical_layout.addWidget(self.tree_widget)

        self.remove_category_button = QPushButton()
        self.remove_category_button.setText("Удалить категорию со всеми подкатегориями")
        self.remove_category_button.setStyleSheet(
            "color: white;\n"
            "background-color: rgb(11, 121, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )
        self.vertical_layout.addWidget(self.remove_category_button)

        self.setLayout(self.vertical_layout)
