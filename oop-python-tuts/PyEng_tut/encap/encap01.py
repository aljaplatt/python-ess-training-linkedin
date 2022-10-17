
#* encapsulation is the mechanism of hiding data implementation, keeping instance variables private. 
#? Restrict access to getter/setters, instance methods - only used internally not externally.


#todo - we want to keep the salary private 
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 500 #! the _ does not make private, just signals it should be private / internal 
        self._num_bugs_solved = 0 

se = SoftwareEngineer("Alex", 35)
print(se.name, se.age) # Alex 35
print(se.name, se.age, se._salary) # Alex 35 500

#? the single underscore _x is known as a protected attribute 
