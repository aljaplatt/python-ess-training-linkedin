
class Tire:
    '''
    Defines an automobile tire object.
    :param type: the type of tyre, e.g. wet, off-road, winter
    :param distance_covered: the distance in km the tire has travelled 
    '''
    def __init__(self, type, distance_covered):
        self.type = type
        self.distance_covered = distance_covered


class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"
    tires = [Tire("wet", 100) for i in range(4)]

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

#* Mutability  
# immutables - booleans, ints, floats, strings, tuples


print(m1.tires)
# [<__main__.Tire object at 0x10523ff40>, 
# <__main__.Tire object at 0x10523fd60>, 
# <__main__.Tire object at 0x10523fd00>, 
# <__main__.Tire object at 0x10523fca0>]

#! PROBLEM - m2 has the same tire objects as m1 - they share the same tires!

print(m2.tires)
# [<__main__.Tire object at 0x10523ff40>, 
# <__main__.Tire object at 0x10523fd60>, 
# <__main__.Tire object at 0x10523fd00>, 
# <__main__.Tire object at 0x10523fca0>]

#! if for some reason we add another tyre to m1, they both get new tyres.
m1.tires.append(Tire(type="spare", distance_covered=0))

print(m1.tires)
print(m2.tires)

#* They both share the same mutable class variable, so when that variable is modified - all class instances are also modified, even new mercedes will have 5 tires!
#todo - good idea not to avoid using mutable data structures as class variables  