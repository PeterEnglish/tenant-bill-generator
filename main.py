class Bill:
    """
    Object that contains data about a bill
    such as total amount and period of bill
    """
    def __init__(self, amount, period): #'self is the default paramter for default 'init' constructor method.
        self.amount = amount # create instances variable
        self.period = period #create instance variable

    
class Flatmate:
    """
    Creates a flatmate object who lives in
     the flat and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount/2


class PdfReport:
    """"
    Creates a pdf file that contains data about
    flatmate such as their names, their due amount
     and the period of the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass



bill = Bill(amount = 120, period= "March 2021")
john = Flatmate(name="John McGrath", days_in_house=20)
mary = Flatmate(name="Mary Walsh", days_in_house=25)
print(john.pays(bill))