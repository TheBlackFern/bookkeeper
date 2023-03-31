"""
Pop up for adding in a category class module.
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
        self.gridLayout = QGridLayout()
        self.setNameLine = QLineEdit()
        self.buttonBox = QDialogButtonBox()
        self.selectCategoryBox = QComboBox()
        self.label_3 = QLabel()
        self.label_5 = QLabel()

        self.resize(518, 171)

        self.gridLayout.setObjectName("gridLayout")
        self.label_3.setObjectName("label_3") 
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_3.setText("Название")

        self.setNameLine.setObjectName("setNameLine")

        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_5.setText("Родительская<br>категория")

        self.selectCategoryBox.setObjectName("selectCategoryBox")
        self.selectCategoryBox.addItems(["-"] + [cat for (cat, _) in cats])

        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal) # type: ignore[attr-defined]
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) # type: ignore[attr-defined]
        self.buttonBox.accepted.connect(self.accept) # type: ignore[attr-defined]
        self.buttonBox.rejected.connect(self.reject) # type: ignore[attr-defined]

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.setNameLine, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.selectCategoryBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.setLayout(self.gridLayout)
