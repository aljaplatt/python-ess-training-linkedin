
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

    #?  check if 2 customers are equal 
    #* By default it compares by memory location - not content 
    #todo - we can override this behaviour 
    # def __eq__(self, other):
    #     if self.name == other.name and self.membership_type == other.membership_type:
    #         return True
    #     return False


# customers = [
#     Customer("Alex", "Platinum"), 
#     Customer("Kelly", "Gold")
# ]

# print(customers[0] == customers[1]) # False

customers = [
    Customer("Alex", "Platinum"), 
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]

print(customers[0] == customers[1]) # True
print(id(customers[0]), id(customers[1])) # 4301782992 4301782608 - different memory location 

#? comment out __eq__ method and this would be false 
