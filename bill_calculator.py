class BillCalculator:
    """
    Takes the property and the flatmates as paramaters
    and allows you to calulate the total bill based on 
    their rent. Also includes a percentage rent method.
    """
    def __init__(self, property, *flatmates):
        self.property = property
        self.flatmates = flatmates
        
    def calculate_bill(self):
        bill = 0
        for flatmate in self.flatmates:
            bill += flatmate.monthly_room_cost
        return bill
    
    def calculate_total_per_flatmate(self):
        totals_per_flatmate = {}
        for flatmate in self.flatmates:
            totals_per_flatmate[flatmate.name] = flatmate.monthly_room_cost
        return totals_per_flatmate


    def calculate_percentage_per_flatmate(self):
        percentages = {}
        for flatmate in self.flatmates:
            percentages[flatmate.name] = "{:.2f}".format(float(flatmate.monthly_room_cost/self.calculate_bill()))
        return percentages