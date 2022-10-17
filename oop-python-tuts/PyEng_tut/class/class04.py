
#? class
class SoftwareEngineer:

    #? class attribute 
    alias = "Keyboard warrior"
    
    def __init__(self, name, age, level, salary):
        # instance attribute - only belongs to the created object, not the class.
        self.name = name
        self.age  = age
        self.level = level
        self.salary = salary

    # instance method
    # tie this to the class - only instances of software engineer class 'can write code'
    def code(self):
        print(f"{self.name} is writing code.")
    
    # we can pass in our own parameters
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}.")
    
    # def info(self):
    #     return f"name = {self.name}, age= {self.age}, level= {self.level}"

    # dunder methods
    def __str__(self):
        #? executed when our object is converted to a string (we try to print obj)
        return f"name = {self.name}, age= {self.age}, level= {self.level}"


se1 = SoftwareEngineer("Alex", 25, "Senior", 9000)
se2 = SoftwareEngineer("Jo", 35, "Boss", 19000)

# self is automatically passed in. 
se1.code() # Alex is writing code.
se2.code() # Jo is writing code.

se1.code_in_language("python")
se2.code_in_language("java")

# print(se1.info())
# print(se2.info())

# without __str__()
print(se1)  # <__main__.SoftwareEngineer object at 0x104b73fd0>

# with __str__()
print(se1) # name = Alex, age= 25, level= Senior