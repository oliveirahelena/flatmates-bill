import os
import webbrowser

from filestack import Client
from flat import Bill, Flatmate
from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("app/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        os.chdir("app/files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileSharer:
    def __init__(
        self, filepath: str, api_key: str = "INSERT YOUR API KEY HERE"
    ) -> None:
        self.filepath = filepath
        self.api_key = api_key

    def share(self) -> str:
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
