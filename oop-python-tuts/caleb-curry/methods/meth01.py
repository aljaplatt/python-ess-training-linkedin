
class Customer:
    #* init method - define attribute we want attached to each object
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership


customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]


print(customers[1].membership_type) # Gold
customers[1].update_membership("Platinum")
print(customers[1].membership_type) # Platinum


# customer created
# Alex Platinum