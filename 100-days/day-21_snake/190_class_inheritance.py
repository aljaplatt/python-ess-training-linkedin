class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

#? fish is inheriting from the animal class - (Animal) = super class
class Fish(Animal):
    def __init__(self):
        #? get hold of animal attributes and methods use super class to call initialiser 
        # inherit all attr and methods from super class  
        super().__init__()

    def breathe(self):
        super().breathe() #* allows the action of animal class to occur - print("Inhale, exhale.")
        # then do the new thing - below
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()