import webbrowser

from fpdf import FPDF
class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate name who lives in the flat and pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    create a Pdf file that contains data about the flatmates such as their names ,
    their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P" ,unit="pt" ,format="A4")
        pdf.add_page()

        pdf.image("house.png",w=30,h=30)

        pdf.set_font("Times","B",24)
        pdf.cell(w=0,h=80,txt="Flatmate bill" ,align="C",ln=1)

        pdf.cell(w=100,h=40,txt="Period:")
        pdf.cell(w=150,h=40,txt=bill.period,ln=1)

        pdf.cell(w=100,h=40,txt=flatmate1.name)
        pdf.cell(w=150,h=40,txt=str(round(flatmate1.pays(bill,flatmate2),2)),ln=1)
        pdf.cell(w=100, h=40,txt=flatmate2.name)
        pdf.cell(w=150,h=40,txt=str(round(flatmate2.pays(bill,flatmate1),2)),ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)

the_bill = Bill(120, "March 2024")
jai = Flatmate("Jai", 20)
jaya = Flatmate("Jaya", 25)
print("jai pays", jai.pays(the_bill, jaya))
print("jaya pays", jaya.pays(the_bill, jai))

pdf_report = PdfReport("Report.pdf")
pdf_report.generate(jai,jaya,the_bill)
