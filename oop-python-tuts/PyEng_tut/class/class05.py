
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

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


se1 = SoftwareEngineer("Alex", 25, "Senior", 9000)
se2 = SoftwareEngineer("Jo", 35, "Boss", 19000)
se3 = SoftwareEngineer("Jo", 35, "Boss", 19000)

# without __eq__()
print(se2 == se3) #? false - compares memory address, which is different
# with __eq__()
print(se2 == se3) #? True - compares specified attributes - which are the same in this case 





