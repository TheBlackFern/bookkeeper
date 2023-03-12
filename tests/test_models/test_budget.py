"""
Budget class tests.
"""
from bookkeeper.models.budget import Budget


def test_create_with_full_args_list():
    """
    The class should be correctly initialised.
    """
    bgt = Budget(
        amount=100,
        pk=1,
    )
    assert bgt.amount == 100
    assert bgt.pk == 1
