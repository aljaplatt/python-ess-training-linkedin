
#? class
class SoftwareEngineer:
    
    def __init__(self, name, age, level, salary):
        #? these instance attributes are passed in from the outside, when creating the instance object. 
        self.name = name
        self.age  = age
        self.level = level
        self.salary = salary


#* the __init__ method initialises our instance object. 
#* This method defines our instance attributes
#* The first argument it takes is always self. 

#? instance of the software engineer class - we add the instance attributes here.
se1 = SoftwareEngineer("Alex", 25, "Senior", 9000)

# when you create the instance of the class, you input the actual data. You can then access the attributes using dot notation.

print(se1.name) # Alex