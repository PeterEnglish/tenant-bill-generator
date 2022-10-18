class Tenant:
    """
    Creates a tenant object who lives in
    the flat and pays a share of the bill
    """
    def __init__(self, name, phone_number, email, monthly_room_cost):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.monthly_room_cost = round(float(monthly_room_cost),2)