
class Dog:
    def __init__(self, name):
        self.name = name

    # method = function inside class
    def bark(self):
        print("Bark")

    def add_one(self, x):
        return x + 1
    
    @property 
    def name(self):
        print("getter")
        return self._name
    
    # need setter for getter to work ?
    @name.setter
    def name(self, name):
        self._name = name

    

dog_rover = Dog("Rover")
dog_viggo = Dog("Viggo")

print("Dog names: ", dog_rover.name, dog_viggo.name)

