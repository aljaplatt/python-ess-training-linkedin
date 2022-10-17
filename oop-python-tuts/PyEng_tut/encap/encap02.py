
#* encapsulation is the mechanism of hiding data implementation, keeping instance variables private. 
#? Restrict access to getter/setters, instance methods - only used internally not externally.

#todo - we want to keep the salary private 
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 500 #! a double __ will make it inaccessible
        self._num_bugs_solved = 0 

se = SoftwareEngineer("Alex", 35)
print(se.name, se.age) # Alex 35
print(se.name, se.age, se.__salary) # Alex 35 

#* print will raise an attribute error  
#! AttributeError: 'SoftwareEngineer' object has no attribute '__salary'

#? The double underscore is not widely used, just the single _ 
#* the double underscore __x is known as a private attribute 
