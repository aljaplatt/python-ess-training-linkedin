# polymorphism - use a c;ass like its parent but also have child unique properties

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
    # extend - polymorphism 
    def work(self):
        print(f"{self.name} is coding...")

    # extend
    def debug(self):
        print(f"{self.name} is debugging...")


#! child
class Designer(Employee):
    # extend - polymorphism 
    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")


se = SoftwareEngineer("Alex", 35, 2000, "Junior") # inherits name, age from Employee

d = Designer("Ebony", 27, 1900)

employees = [
    SoftwareEngineer("Kevin", 23, 3000, "Mid"),
    SoftwareEngineer("Julie", 30, 4000, "Senior"),
    Designer("Jasmine", 26, 5000)
            ]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

# Kevin is coding...
# Julie is coding...
# Jasmine is designing...