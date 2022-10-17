
from lib2to3.pgen2.token import RPAR


class Customer:
    #* init method - define attribute we want attached to each object
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership

    # invoked anytime we want to 'convert' Customer to a string 
    def __str__(self):
        print("converting to a string")


customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]

#! TypeError: __str__ returned non-string (type NoneType) 
# you need to return a string 
print(customers[1])
