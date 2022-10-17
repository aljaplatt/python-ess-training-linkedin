
#? class
from keyword import softkwlist


class SoftwareEngineer:

    #? class attribute 
    alias = "Keyboard warrior"
    
    def __init__(self, name, age, level, salary):
        # instance attribute - only belongs to the created object, not the class.
        self.name = name
        self.age  = age
        self.level = level
        self.salary = salary

    # @staticmethod - allows you to apply to instance or class - cannot access self attributes.
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


    # def __eq__(self, other):
    #     return self.name == other.name and self.age == other.age

se1 = SoftwareEngineer("Alex", 25, "Senior", 9000)
se2 = SoftwareEngineer("Jo", 35, "Boss", 19000)
se3 = SoftwareEngineer("Jo", 35, "Boss", 19000)

print('34: ', se1.entry_salary(24)) # 5000 = WITH STATIC METHOD 
#! TypeError: SoftwareEngineer.entry_salary() takes 1 positional argument but 2 were given
#? 2 were given - even only 24 was passed in, but because we're using an instance (se1), self was automatically passed in = 2 args 
#* as we didnt use the self parameter we cannot use this on an instance, just the class 

# print(SoftwareEngineer.entry_salary(27)) # 7000

# we can add the @staticmethod decorator - #! this will allow use with instance, but cannot use instance attributes like below

# def entry_salary(age):
    # if self.age < 25: #? this will break - self not defined 
#         return 5000
#     if age < 30:
#         return 7000
#     return 9000





