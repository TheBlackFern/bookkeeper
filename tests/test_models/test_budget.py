"""
Budget class tests.
"""
from bookkeeper.models.budget import Budget


# import pytest
# from bookkeeper.repository.memory_repository import MemoryRepository
# from bookkeeper.repository.abstract_repository import RepositoryProtocol
# @pytest.fixture(name="repo")
# def fixture_repository():
#     """
#     A fixture to text repository integration of the class.
#     """
#     return MemoryRepository()


def test_create_with_full_args_list():
    """
    The class should be correctly initialised.
    """
    bgt = Budget(
        amount=100,
        period="day",
        pk=1,
    )
    assert bgt.amount == 100
    assert bgt.period == "day"
    assert bgt.get_spent() == 0


def test_can_add_expense():
    """
    The class should correctly update spent value.
    """
    bgt = Budget(1000, "day")
    bgt.count_in(100)
    assert bgt.get_spent() == 100
    bgt.count_in(200)
    assert bgt.get_spent() == 300
