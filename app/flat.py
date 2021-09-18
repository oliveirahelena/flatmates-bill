from __future__ import annotations


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount: float, period) -> None:
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatemate person who lives in the flat and pays a share of a bill.
    """

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, other: Flatmate) -> float:
        weight = self.days_in_house / (self.days_in_house + other.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
