
from lib2to3.pgen2.token import RPAR


class Customer:
    #* init method - define attribute we want attached to each object
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    #todo - invoked anytime we want to 'convert' Customer to a string 
    def __str__(self):
        print("converting to a string")
        return self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)


customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]


# print(customers[1])
# converting to a string
# Kelly Gold

Customer.print_all_customers(customers)
'''
converting to a string
Alex Platinum
converting to a string
Kelly Gold
'''