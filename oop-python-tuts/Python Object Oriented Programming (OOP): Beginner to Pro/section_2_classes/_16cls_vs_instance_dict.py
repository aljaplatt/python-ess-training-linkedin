
#todo - class vs instance dict  

#* classes also have their own namespace that can be accessed in the same way, using __dict__

from _15dunder_dict import MercedesBenz, m1

print(MercedesBenz.__dict__)
print(type(MercedesBenz.__dict__)) #? <class 'mappingproxy'>
'''
#? dunder module retrieves the module where the class was defined.
{'__module__': '_15dunder_dict', 
'doors': 4, 
'wheels': 4, 
'model': 'G', 
'__init__': <function MercedesBenz.__init__ at 0x102a1b640>, 
'drive': <function MercedesBenz.drive at 0x102a1a440>, 
'auto_drive': <staticmethod(<function MercedesBenz.auto_drive at 0x102a19bd0>),
#? dict, weakref are descriptors
'__dict__': <attribute '__dict__' of 'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, 
#? dunder doc enables docstrings 
'__doc__': None}
'''

#? This actually returns a mapping proxy, not an object like with an instance, but similar to an object.
#* For performance reasons it is a read-only, and ensures that the look-up keys are always strings. 

#* whenever a attribute or method is accesses from an instance or class, python does an attribute look up

#? descriptors are used to retrieve pointers from instance memory layouts

m1.__dict__ #? __dict__ is not actually in the m1 instance namespace, it is inherited from the class namespace. 
#* When we access dunder dict from an instance, we're asking python to give us the value associated with an attribute called __dict__.
#? It checks the instance namespace, then the class namespace.
#?  Finding __dict__, containing the descriptor -<attribute '__dict__' of 'MercedesBenz' objects>
#* The descriptors 'get()' method is called, which returns the dict pointer, an address in memory for the dict, which gives us the instance namespace -- {'colour': 'Red', 'horse_power': 290}
