"""
Expense class module.
"""
from dataclasses import dataclass


@dataclass(slots=True)
class Expense:
    """
    Expense operation.

    amount - expense sum
    category - expense Category id
    expense_date - the date that expense happened
    comment - additional info on the expense
    pk - id for the repo
    """

    expense_date: str
    amount: str
    category: str
    comment: str = ""
    pk: int = 0
