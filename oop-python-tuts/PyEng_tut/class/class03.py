
#? class
class SoftwareEngineer:

    #? alias is a class attribute - all objects will have this attribute - can be used on the class itself
    alias = "Keyboard warrior"
    
    def __init__(self, name, age, level, salary):
        # instance attribute - only belongs to the created object, not the class.
        self.name = name
        self.age  = age
        self.level = level
        self.salary = salary

se1 = SoftwareEngineer("Alex", 25, "Senior", 9000)
se2 = SoftwareEngineer("Jo", 35, "Boss", 19000)

print(se1.name) # Alex
print(se2.name) # Jo
print(se1.alias) # Keyboard warrior
print(SoftwareEngineer.alias) # Keyboard warrior