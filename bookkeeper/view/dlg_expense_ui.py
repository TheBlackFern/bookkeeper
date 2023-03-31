"""
Pop up for adding in an expense class module.

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
        self.grid_layout = QGridLayout()
        self.grid_layout_widget = QWidget()
        self.button_box = QDialogButtonBox()
        self.set_date_line = QLineEdit()
        self.set_sum_line = QLineEdit()
        self.select_category_box = QComboBox()
        self.set_comment_line = QLineEdit()
        self.add_category_button = QPushButton()
        self.label_3 = QLabel()
        self.label_4 = QLabel()
        self.label_5 = QLabel()
        self.label_6 = QLabel()

        self.resize(450, 258)

        self.button_box.setOrientation(Qt.Horizontal)  # type: ignore[attr-defined]
        self.button_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok  # type: ignore[attr-defined]
        )
        self.button_box.accepted.connect(self.accept)  # type: ignore[attr-defined]
        self.button_box.rejected.connect(self.reject)  # type: ignore[attr-defined]

        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_3.setText("Дата")

        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_4.setText("Сумма")

        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_5.setText("Категория")

        self.label_6.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_6.setText("Комментарий")

        self.set_date_line.setAutoFillBackground(False)
        self.set_date_line.setPlaceholderText("ГГГГ-ММ-ДД")

        self.select_category_box.setObjectName("selectCategoryBox")
        self.select_category_box.addItems([cat for (cat, _) in cats])

        self.set_comment_line.setObjectName("setCommentLine")

        self.grid_layout.addWidget(self.label_3, 0, 0, 1, 3)
        self.grid_layout.addWidget(self.label_4, 1, 0, 1, 3)
        self.grid_layout.addWidget(self.label_5, 2, 0, 1, 3)
        self.grid_layout.addWidget(self.label_6, 3, 0, 1, 3)
        self.grid_layout.addWidget(self.set_date_line, 0, 3, 1, 8)
        self.grid_layout.addWidget(self.set_sum_line, 1, 3, 1, 8)
        self.grid_layout.addWidget(self.select_category_box, 2, 3, 1, 8)
        self.grid_layout.addWidget(self.set_comment_line, 3, 3, 1, 8)
        self.grid_layout.addWidget(self.button_box, 4, 5, 1, 4)
        self.setLayout(self.grid_layout)
