# class MercedesBenz:
#     doors = 4
#     wheels = 4
#     model = "G"

#     def drive(self):
#         print(f"A mercedes is driving. It is {self}\n")
    

# m1 = MercedesBenz()
# m2 = MercedesBenz()

#? both have 4 doors - how could we say m1 has 2 doors, or m2 is red ?
# print(m1.doors) #? we could use m1.doors = 2
# print(m2.doors) #? m2.colour = "red"

#* However the correct way to do this is during the instance initialisation
#TODO - we do this using the __init__ method. 

class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"
    # methods that implement special behaviour - dunder methods __???__
    def __init__(self): # dunder __init__ is called automatically after the instance is created but before the instance is returned.
        pass

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    

m1 = MercedesBenz()
m2 = MercedesBenz()