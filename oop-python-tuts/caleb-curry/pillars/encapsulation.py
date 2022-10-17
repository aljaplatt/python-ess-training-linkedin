
#? Encapsulation - Hide the inner details of a class, only expose what it needed to use the class

#todo - getters and setters 
#* You only set and get the data through a getter and setter method.

#? @property 

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
    #? underscore = protected or private 
        print("getting name...")
        return self._name
    

    @name.setter
    def name(self, name):
        print("setting name...")
        self._name = name
    
    def __str__(self):
        return f"{self.name} {self.membership_type}"
    
    __repr__ = __str__


customers = [
    Customer("Kelly", "Gold"),
    Customer("Alan", "Old")
    ]

# print(customers)
'''
setting name...
setting name...
getting name...  # __repr__ = __str__
getting name...  # __repr__ = __str__
[Kelly Gold, Alan Old]  # __repr__ = __str__
'''

print(customers[0].name)