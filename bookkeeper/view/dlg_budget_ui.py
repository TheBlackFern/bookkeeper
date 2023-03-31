"""
Pop up for changeing budget class module.

"type: ignore[attr-defined]" comments are here becose or C++ nature of PySide
which erroniously doesn't see many attributes and methods PySide objects have.
"""

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QWidget,
)


class DialogBudget(QDialog):
    """
    Class for a pop up for changing the budget.
    Has three lines, for budgets for a month, week and day, that are all labelled.
    """
    def __init__(self) -> None:
        super().__init__()
        self.resize(386, 185)
        self.setWindowTitle("Установка бюджета")

        self.grid_layout_widget = QWidget()
        self.grid_layout_widget.setObjectName("gridLayoutWidget")
        self.grid_layout_widget.setGeometry(QRect(20, 0, 341, 141))

        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setObjectName("gridLayout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel(self.grid_layout_widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 11pt\n")
        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_4.setText("Бюджет на неделю:")

        self.grid_layout.addWidget(self.label_4, 1, 0, 1, 1)

        self.set_day_budget_line = QLineEdit(self.grid_layout_widget)
        self.set_day_budget_line.setObjectName("setSumLine")
        self.set_day_budget_line.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )

        self.grid_layout.addWidget(self.set_day_budget_line, 0, 1, 1, 1)

        self.label_3 = QLabel(self.grid_layout_widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 11pt\n")
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_3.setText("Бюджет на день:")

        self.grid_layout.addWidget(self.label_3, 0, 0, 1, 1)

        self.set_week_budget_line = QLineEdit(self.grid_layout_widget)
        self.set_week_budget_line.setObjectName("setSumLine_2")
        self.set_week_budget_line.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )

        self.grid_layout.addWidget(self.set_week_budget_line, 1, 1, 1, 1)

        self.set_month_budget_line = QLineEdit(self.grid_layout_widget)
        self.set_month_budget_line.setObjectName("setSumLine_3")
        self.set_month_budget_line.setStyleSheet(
            "background-color: rgb(255,255, 255);\n" +
            "font: 11pt;\n" +
            "border-radius: 10px"
        )

        self.grid_layout.addWidget(self.set_month_budget_line, 2, 1, 1, 1)

        self.label_5 = QLabel(self.grid_layout_widget)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font: 11pt\n")
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter  # type: ignore[attr-defined]
        )
        self.label_5.setText("Бюджет на месяц:")

        self.grid_layout.addWidget(self.label_5, 2, 0, 1, 1)

        self.button_box = QDialogButtonBox()
        self.button_box.setObjectName("buttonBox")
        self.button_box.setGeometry(QRect(80, 140, 201, 32))
        self.button_box.setOrientation(Qt.Horizontal)  # type: ignore[attr-defined]
        self.button_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok  # type: ignore[attr-defined]
        )
        self.button_box.accepted.connect(self.accept)  # type: ignore[attr-defined]
        self.button_box.rejected.connect(self.reject)  # type: ignore[attr-defined]

        self.grid_layout.addWidget(self.button_box, 3, 0, 1, 2)

        self.setLayout(self.grid_layout)
