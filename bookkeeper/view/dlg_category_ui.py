"""
Pop up for adding in a category class module.

"type: ignore[attr-defined]" comments are here becose or C++ nature of PySide
which erroniously doesn't see many attributes and methods PySide objects have.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
)


class DialogCategory(QDialog):
    """
    Class for a pop up for adding in a category.
    Has two lines, for a category name and its parent category, that are all labelled.
    """
    def __init__(self, cats: list[tuple[str, str | None]]) -> None:
        super().__init__()
        self.setWindowTitle("Добавление категории")
        self.grid_layout = QGridLayout()
        self.set_name_line = QLineEdit()
        self.button_box = QDialogButtonBox()
        self.select_category_box = QComboBox()
        self.label_3 = QLabel()
        self.label_5 = QLabel()

        self.resize(518, 171)

        self.grid_layout.setObjectName("gridLayout")
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_3.setText("Название")

        self.set_name_line.setObjectName("setNameLine")

        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_5.setText("Родительская<br>категория")

        self.select_category_box.setObjectName("selectCategoryBox")
        self.select_category_box.addItems(["-"] + [cat for (cat, _) in cats])

        self.button_box.setObjectName("buttonBox")
        self.button_box.setOrientation(Qt.Horizontal)  # type: ignore[attr-defined]
        self.button_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok  # type: ignore[attr-defined]
        )
        self.button_box.accepted.connect(self.accept)  # type: ignore[attr-defined]
        self.button_box.rejected.connect(self.reject)  # type: ignore[attr-defined]

        self.grid_layout.addWidget(self.label_3, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.set_name_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.label_5, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.select_category_box, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button_box, 2, 1, 1, 1)
        self.setLayout(self.grid_layout)
