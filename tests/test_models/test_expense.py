"""
Expense class tests.
"""
from datetime import datetime

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.expense import Expense


@pytest.fixture(name="repo")
def fixture_repository():
    """
    A fixture to text repository integration of the class.
    """
    return MemoryRepository()


def test_create_with_full_args_list():
    """
    The class should be correctly initialised.
    """
    exp = Expense(
        amount="100",
        category="bakery",
        expense_date="2023-12-12",
        comment="test",
        pk=1,
    )
    assert exp.amount == "100"
    assert exp.category == "bakery"


def test_can_add_to_repo(repo):
    """
    A repository should have no trouble adding an instance of the class.
    """
    exp = Expense(
        amount="100",
        category="bakery",
        expense_date="2023-12-12",
        comment="test",
    )
    pk = repo.add(exp)
    assert exp.pk == pk
