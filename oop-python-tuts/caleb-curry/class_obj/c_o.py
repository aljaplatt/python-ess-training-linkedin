
class Customer:
    # initialiser / constructor function
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("customer created")

# c = Customer("Alex", "Platinum")
# c2 = Customer("Kelly", "Gold")
# print(c.name, c.membership_type)

#? this way is better if you have a large number of objects
customers = [
    Customer("Alex", "Platinum"), 
    Customer("Kelly", "Gold")
]

print(customers[0]) # <__main__.Customer object at 0x100fdae30>
print(customers[0].name) # Alex
print(customers[1].name) # Kelly


# customer created
# Alex Platinum