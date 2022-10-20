# gettattr is a built in python function

class MercedesBenz:
    doors = 4
    wheels = 4
    model = "G"

    def __init__(self, colour): 
        self.colour = colour

    def drive(self):
        print(f"A mercedes is driving. It is {self}\n")

m1 = MercedesBenz("Red")
m2 = MercedesBenz("Black")

print(getattr(m1, "colour")) # Red 
setattr(m1, "colour", "blue")
print(getattr(m1, "colour")) # Blue

#? Why? - useful when you need to manipulate objects programmatically at scale, if you have lots. With the dot method, you'd have to change one by one

objs = [m1, m2]

attribs = ["colour", "doors"]
values = ["navy", 3]

# iterate over objs 
for obj in objs:
    for attrib, val in zip(attribs, values):
        setattr(obj, attrib, val)

# print(m1.colour, m2.colour) # navy navy

#? zip detour - zip provides a zip object, an iterable
print(zip(attribs, values)) # <zip object at 0x102c7db80>

# we iterate over [('colour', 'navy'), ('doors', 3)]
print(list(zip(attribs, values))) #* [('colour', 'navy'), ('doors', 3)]
# we reach into the first tuple and assign attrib to colour and val to navy, then attrib to door and val to three

# we then call setattr on the object

try:
    print(m2.wingspan)
except AttributeError as e:
    print(e) # 'MercedesBenz' object has no attribute 'wingspan'

print(getattr(m2, "wingspan", "No wingspan attribute found")) # No wingspan attribute found