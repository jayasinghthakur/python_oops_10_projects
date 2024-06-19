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
        pass


the_bill = Bill(120, "March 2024")
jai = Flatmate("Jai", 20)
jaya = Flatmate("Jaya", 25)
print("jai pays", jai.pays(the_bill, jaya))
print("jaya pays", jaya.pays(the_bill, jai))
