class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): 
        self.colour = colour

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    
    #todo RECAP - functions defined in the class body are assumed to be instance methods, and are automatically passed 'self' as an argument.
    #* However we may not want solely an instance method, we may want to call it from the class. We can do this using the @staticmethod decorator. 
    @staticmethod
    def auto_drive():
        # doesnt require access to instance attributes 
        print("Auto-driving")
        return "Auto-driving"

m1 = MercedesBenz("Red")
m2 = MercedesBenz("Black")

m1.auto_drive()
MercedesBenz.auto_drive() #! without decorator -TypeError: MercedesBenz.auto_drive() takes 0 positional arguments but 1 was given 
#? with decorator - Auto-driving
