

#? inheritence - one class takes on the attributes of another class

#* child inherits from parent 
#! parent/base class
class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self):
        print(f"{self.name} is working...")


#? Children inherit all the attributes and methods from parent
#* inherits, extends, override 
#! child
class SoftwareEngineer(Employee):
    pass


#! child
class Designer(Employee):
    pass 


se = SoftwareEngineer("Alex", 35) # inherits name, age from Employee
print(se.name, se.age) # Alex 35
print(se.work())

d = Designer("Ebony", 27)
print(d.name, d.age) # Ebony 27
print(d.work())