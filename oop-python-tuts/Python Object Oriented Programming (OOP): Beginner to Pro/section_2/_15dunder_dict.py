
#* Dunder dict - instance namespace 

class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): 
        self.colour = colour


    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    

    def auto_drive():
        print("Auto-driving")
        return "Auto-driving"

m1 = MercedesBenz("Red")
m2 = MercedesBenz("Black")

#* we can access instance attributes using 'object.attribute' syntax
print(m1.colour) # Red 

#? Where does this attribute, or where is the binding between instance object and attribute stored? 
#* All instance attributes are stored in an instance specific, mapping object (essentially a python object) that can be accessed using dunder dict __dict__. 

print(m1.__dict__) # {'colour': 'Red'}
print(m2.__dict__) # {'colour': 'Black'}

#todo - m1 and m2 share the same MercedesBenz class, or blueprint, they do not share the same namespace 

m2.horse_power = 490
print(m1.__dict__) # {'colour': 'Red'}
print(m2.__dict__) # {'colour': 'Black', 'horse_power': 490}

m1.__dict__["horse_power"] = 290
print(m1.__dict__) # {'colour': 'Red', 'horse_power': 290}

#? __dict__ is a class attribute and lives in the namespace of the class, it is passed down to class instances through inheritance 

