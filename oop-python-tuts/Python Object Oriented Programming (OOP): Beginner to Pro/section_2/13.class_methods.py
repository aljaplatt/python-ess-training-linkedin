class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): 
        self.colour = colour

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")
    
    @staticmethod
    def auto_drive():
        print("Auto-driving")
        return "Auto-driving"
    
    @classmethod
    def create_lease(cls):
        print(f"A lease for {cls} will be created")

m1 = MercedesBenz("Red")
m2 = MercedesBenz("Black")

MercedesBenz.create_lease() 
#? A lease for <class '__main__.MercedesBenz'> will be created

m1.create_lease() # calling from the instance has the same result
#? A lease for <class '__main__.MercedesBenz'> will be created

#todo - The key difference between class and static methods is that class methods automatically receive the class (cls) as the first argument 

#* this allows class methods to modify class state or behaviour at runtime

#? static methods allow you to add conceptually related, regular functions to the class, that do not need access to the class state, self. 