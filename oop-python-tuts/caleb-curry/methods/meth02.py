
from lib2to3.pgen2.token import RPAR


class Customer:
    #* init method - define attribute we want attached to each object
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    #todo -  method without self?
    def read_customer():
        print("Reading customer from DB...")


customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]

customers[0].read_customer()

#! TypeError: Customer.read_customer() takes 0 positional arguments but 1 was given 

#* This will not work as customers[0] is automatically passed the self attribute - 1 positional argument. However, the read_customer method expects no arguments.

#? In this case, reading a customer from the DB isn't related to the specific customer, but the class

#todo  This will work
# Customer.read_customer()

