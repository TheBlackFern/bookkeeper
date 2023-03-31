"""
Pop up for changeing budget class module.
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

        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 0, 341, 141))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 11pt\n" "")
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_4.setText("Бюджет на неделю:")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.setDayBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setDayBudgetLine.setObjectName("setSumLine")
        self.setDayBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )

        self.gridLayout.addWidget(self.setDayBudgetLine, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 11pt\n" "")
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_3.setText("Бюджет на день:")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.setWeekBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setWeekBudgetLine.setObjectName("setSumLine_2")
        self.setWeekBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )

        self.gridLayout.addWidget(self.setWeekBudgetLine, 1, 1, 1, 1)

        self.setMonthBudgetLine = QLineEdit(self.gridLayoutWidget)
        self.setMonthBudgetLine.setObjectName("setSumLine_3")
        self.setMonthBudgetLine.setStyleSheet(
            "background-color: rgb(255,255, 255);\n"
            "font: 11pt;\n"
            "border-radius: 10px"
        )

        self.gridLayout.addWidget(self.setMonthBudgetLine, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font: 11pt\n" "")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter) # type: ignore[attr-defined]
        self.label_5.setText("Бюджет на месяц:")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QRect(80, 140, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal) # type: ignore[attr-defined]
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) # type: ignore[attr-defined]
        self.buttonBox.accepted.connect(self.accept) # type: ignore[attr-defined]
        self.buttonBox.rejected.connect(self.reject) # type: ignore[attr-defined]

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.setLayout(self.gridLayout)
