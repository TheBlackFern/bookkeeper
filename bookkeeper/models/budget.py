"""
Budget class module.
"""
from dataclasses import dataclass


@dataclass(slots=True)
class Budget:
    """
    Budget for a certain for a certain period of time.

    amount - sum of money allocated
    pk - id in the database
    """

    amount: float
    pk: int = 0
