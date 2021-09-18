from __future__ import annotations

from typing import Union


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount: Union[float, int], period) -> None:
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


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names,
    their due amount and the period of the bill.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self, flatemate1: Flatmate, flatemate2: Flatmate, bill: Bill) -> None:
        pass


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, other=marry))
print("Marry pays: ", marry.pays(bill=the_bill, other=john))
