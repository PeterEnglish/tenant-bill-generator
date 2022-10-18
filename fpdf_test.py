from distutils.command.build_scripts import first_line_re
from fpdf import FPDF
import datetime
import calendar
currentDate = datetime.date.today()
first_day_of_month = datetime.date(currentDate.year, currentDate.month, 1)
first_day_of_month = first_day_of_month.strftime("%d-%m-%Y")
last_day_of_month = datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[-1])
last_day_of_month = last_day_of_month.strftime("%d-%m-%Y")

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.set_font(family='Arial', size=24, style='B')
pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

pdf.set_font(family='Arial', size=16, style='B')
pdf.cell(w=80, h=40, txt='Period:')

pdf.set_font(family='Arial', size=16, style='B')
pdf.cell(w=100, h=40, txt=f"{first_day_of_month} to {last_day_of_month}")

pdf.output("bill.pdf")