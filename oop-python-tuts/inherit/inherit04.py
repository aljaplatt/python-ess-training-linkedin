

#? inheritence - one class takes on the attributes of another class

#* child inherits from parent 
#! parent/base class
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary 
    
    def work(self):
        print(f"{self.name} is working...")


#? Children inherit all the attributes and methods from parent
#* extends, override 
#! child
class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        # super refer to the parent class - Employee
        super().__init__(name, age, salary)
        self.level = level 
        # level attr only works for software engineer 

    # extend
    def debug(self):
        print(f"{self.name} is debugging...")


#! child
class Designer(Employee):
    # extend
    def draw(self):
        print(f"{self.name} is drawing...")


se = SoftwareEngineer("Alex", 35, 2000, "Junior") # inherits name, age from Employee
print(se.name, se.age, se.level) # Alex 35, junior 
print(se.work())
print(se.debug())
# cannot draw

d = Designer("Ebony", 27, 1900)
print(d.name, d.age) # Ebony 27
print(d.work())
print(d.draw())
# cannot debug 