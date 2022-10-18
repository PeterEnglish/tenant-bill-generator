import datetime
import calendar
from fpdf import FPDF

class PdfReport:
    """"
    Creates a pdf file that contains data about
    flatmate such as their names, their due amount
     and the period of the bill
    """
    def __init__(self, filename, billcalculator):
        self.billcalculator = billcalculator
        self.filename = filename

    def set_regular_font(self, pdf):
        pdf.set_font(family='Arial', size=16, style='')

    def skip_line(self, pdf):
        pdf.cell(w=400, h=40, ln=1, txt="")

    def get_current_date(self):
        currentDate = datetime.date.today()
        first_day_of_month = datetime.date(currentDate.year, currentDate.month, 1)
        first_day_of_month = first_day_of_month.strftime("%d-%m-%Y")
        last_day_of_month = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[-1])
        last_day_of_month = last_day_of_month.strftime("%d-%m-%Y")
        return first_day_of_month + " - " + last_day_of_month

    def generate(self):
        total_bill = self.billcalculator.calculate_bill()
        total_per_flatmate = self.billcalculator.calculate_total_per_flatmate()
        address = self.billcalculator.property

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=80,ln=1, txt=f'Rent Due: {address}', border=1, align='C')

        self.skip_line(pdf)
        pdf.set_font(family='Arial', size=16, style='U')
        pdf.cell(w=80, h=40,ln=1, txt=f'To the Occupants of {address} - Your Rent is Now Due')

        pdf.set_font(family='Arial', size=16, style='U')
        pdf.cell(w=80, h=40, txt='Period:')

        self.set_regular_font(pdf)
        pdf.cell(w=100, h=40,ln=1, txt=f"{self.get_current_date()}")

        self.set_regular_font(pdf)
        pdf.set_font(family='Arial', size=16, style='U')
        pdf.cell(w=100, h=40, txt=f"Total Bill: ")
        pdf.set_font(family='Arial', size=16, style='')
        total_bill_decimal = "{:.2f}".format(total_bill)
        pdf.cell(w=100, h=40, txt=f"${total_bill_decimal}")
        self.skip_line(pdf)
        self.skip_line(pdf)
        
        pdf.set_font(family='Arial', size=16, style='U')
        pdf.cell(w=100, h=40, ln=1, txt="Amount Per Occupant:")

        self.set_regular_font(pdf)
        for key in total_per_flatmate:
            rent_per_flatmate_decimal = "{:.2f}".format(total_per_flatmate[key])
            pdf.cell(w=100, h=40, ln=1, txt=f"{key}: ${rent_per_flatmate_decimal}")

        self.skip_line(pdf)

        pdf.multi_cell(w=500, h=40, txt="Please Note: This amount will be withdrawn by standing order, or alternatively can be paid by cash if standing order is not set up.")
        pdf.output(self.filename)