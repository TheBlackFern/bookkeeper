"""
Pop up for adding in an expense class module.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class DialogExpense(QDialog):
    """
    Class for a pop up for adding in an expense.
    Has four lines, for a date, name, category and a comment, that are all labelled.
    Date line has a background text to hint at date format.
    """
    def __init__(self, cats: list[tuple[str, str | None]]) -> None:
        super().__init__()
        self.setWindowTitle("Добавление траты")
        self.gridLayout = QGridLayout()
        self.gridLayoutWidget = QWidget()
        self.buttonBox = QDialogButtonBox()
        self.setDateLine = QLineEdit()
        self.setSumLine = QLineEdit()
        self.selectCategoryBox = QComboBox()
        self.setCommentLine = QLineEdit()
        self.addCategoryButton = QPushButton()
        self.label_3 = QLabel()
        self.label_4 = QLabel()
        self.label_5 = QLabel()
        self.label_6 = QLabel()

        self.resize(450, 258)

        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal) # type: ignore[attr-defined]
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) # type: ignore[attr-defined]
        self.buttonBox.accepted.connect(self.accept) # type: ignore[attr-defined]
        self.buttonBox.rejected.connect(self.reject) # type: ignore[attr-defined]

        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_3.setText("Дата")

        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_4.setText("Сумма")

        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_5.setText("Категория")

        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_6.setText("Комментарий")

        self.setDateLine.setObjectName("setDateLine")
        self.setDateLine.setAutoFillBackground(False)
        self.setDateLine.setPlaceholderText("ГГГГ-ММ-ДД")

        self.setSumLine.setObjectName("setSumLine")

        self.selectCategoryBox.setObjectName("selectCategoryBox")
        self.selectCategoryBox.addItems([cat for (cat, _) in cats])

        self.setCommentLine.setObjectName("setCommentLine")

        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.setDateLine, 0, 3, 1, 8)
        self.gridLayout.addWidget(self.setSumLine, 1, 3, 1, 8)
        self.gridLayout.addWidget(self.selectCategoryBox, 2, 3, 1, 8)
        self.gridLayout.addWidget(self.setCommentLine, 3, 3, 1, 8)
        self.gridLayout.addWidget(self.buttonBox, 4, 5, 1, 4)
        self.setLayout(self.gridLayout)
