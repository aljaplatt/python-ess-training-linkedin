
#* self represents the instance of the class 
#? when we define methods within the class body, python assumes they are instance methods, and binds them so the first argument the methods receive is always the instance itself - self.
#* self represents the instance object bound to the method. 

class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): 
        self.colour = colour

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    
    #todo - what if we define a method without self, no arguments. 
    # if we pass in self, the TypeError is not raised.
    def auto_drive():
        print("Auto-driving")
        return "Auto-driving"

m1 = MercedesBenz("Red")
m2 = MercedesBenz("Black")

m2.auto_drive() #! TypeError: MercedesBenz.auto_drive() takes 0 positional arguments but 1 was given



