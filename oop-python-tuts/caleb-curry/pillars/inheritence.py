
#? Inheritance allows objects to have access to properties/attributes from a parent, or base class, without having to add the data into the class in question (child class)

            # user

    # customer      teacher 

# user is the base class, customer and teacher will inherit anything defining inside the user class

class User:
    def log(self):
        print(self)


#todo - add the Parent class in brackets to the child class 
#? Then anything defined in User will be available to Customer  
class Customer(User):
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


customers[0].log() # Kelly Gold 