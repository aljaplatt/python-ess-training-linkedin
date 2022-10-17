
#* encapsulation is the mechanism of hiding data implementation, keeping instance variables private. 
#? Restrict access to getter/setters, instance methods - only used internally not externally.

#todo - we want to keep the salary private 
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None #! single _
        self._num_bugs_solved = 0 
    
    #? The get and set methods allow you to modify from the outside 
    #! Getters and setters should be the only way to access the salary attribute 

    def get_salary(self):
        return self._salary
    
    def set_salary(self, value):
        # check value, enforce constraints 
        if value < 1000:
            self._salary = 1000
        if value > 20000:
            self._salary = 20000
        self._salary = value

se = SoftwareEngineer("Alex", 35)

se.set_salary(9000)

se._salary = 10000 #! still works ? - whats the point? - enforce good habits?
print(se.get_salary()) #? 9000 



