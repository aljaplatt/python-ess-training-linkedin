from _17mutables import MercedesBenz, Tire, m1

# help(getattr)

obj = {"name": "Alex", "team": "United", "job": "software engineer"}

name = getattr(m1, "doors")
# print(obj["name"]) # Alex
print(name)  # 4

# help(Tire) #? if we add the a docstring as the top of the class, this will be added to the help info

#* python binds the documentation to the __doc__ class attribute.

print(Tire.__dict__)
'''
{'__module__': '_17mutables', 
'__doc__': '\n    Defines an automobile tire object.\n    
:param type: the type of tyre, e.g. wet, off-road, winter\n    
:param distance_covered: the distance in km the tire has travelled \n    ', 
'__init__': <function Tire.__init__ at 0x1048d6d40>,
'__dict__': <attribute '__dict__' of 'Tire' objects>,
'__weakref__': <attribute '__weakref__' of 'Tire' objects>}
'''
