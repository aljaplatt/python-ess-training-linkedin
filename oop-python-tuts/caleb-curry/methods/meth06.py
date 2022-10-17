
from lib2to3.pgen2.token import RPAR


class Customer:
    #* init method - define attribute we want attached to each object
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership


    def __str__(self):
        print("converting to a string")
        return self.name + " " + self.membership_type
    

    def print_all_customers(customers):
        for customer in customers:
            print(customer)


    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    
    #? Hashing ??
    __hash__ = None

    __repr__ = __str__


customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]

# __repr__ = __str__
print(customers) # [Alex Platinum, Kelly Gold]

