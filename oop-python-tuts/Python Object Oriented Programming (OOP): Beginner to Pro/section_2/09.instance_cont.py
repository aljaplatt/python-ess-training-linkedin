
class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): # after self, we pass into the init method the attributes we want to customise. And then define the blueprint below. Eg: When the instance is created, we cant to customise the colour of this Mercedezbenz object, so we pass in colour on initialisation, then state that the colour attribute, should be whatever is passed in.
        self.colour = colour

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    
# we must pass in the colour for initialisation to work
m1 = MercedesBenz("Red")
# m2 = MercedesBenz() #! TypeError: MercedesBenz.__init__() missing 1 required positional argument: 'colour'
#? The error states we are missing only 1 argument, how the __init__ method, in this case requires 2, self AND colour. 
#* Dunder init is bound to the instance, an instance method. It will automatically receive the instance object, self, as the first argument upon instantiation when the init method is called, you do not need to pass it in. You only need to specify the additional parameters. 
# it is possible to set a default - def __init__(self, colour="black"):, then it is not required

m2 = MercedesBenz("Black")

print(m1.colour) # Red
print(m2.colour) # Black

# notes

# attributes are variables associated with objects 
# it is best practice to set instance attributes during initialisation, using the dunder init method.
