from pdf_generator import PdfReport
from bill_calculator import BillCalculator
from tenant import Tenant

def main():
    tony = Tenant("John McGrath", "0874578695", "johntheboy@gmail.com", 450)
    jill = Tenant("Jill McClean", "0854543734", "jillthegirl@gmail.com", 560)
    michael = Tenant("Michael O'Brien", "0874578643", 'michaeltheman@gmail.com', 560)
    bill_calc = BillCalculator('52 Mercier Court',tony, jill, michael)
    pdf_generator = PdfReport('bill1.pdf',bill_calc)
    pdf_generator.generate()

main()
