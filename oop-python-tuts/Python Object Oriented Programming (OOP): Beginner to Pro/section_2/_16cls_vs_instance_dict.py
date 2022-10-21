
#todo - class vs instance dict  

#* classes also have their own namespace that can be accessed in the same way, using __dict__

from _15dunder_dict import MercedesBenz

print(MercedesBenz.__dict__)
print(type(MercedesBenz.__dict__)) #? <class 'mappingproxy'>
'''
{'__module__': '_15dunder_dict', 'doors': 4, 'wheels': 4, 'model': 'G', '__init__': <function MercedesBenz.__init__ at 0x102a1b640>, 'drive': <function MercedesBenz.drive at 0x102a1a440>, 'auto_drive': <function MercedesBenz.auto_drive at 0x102a19bd0>, '__dict__': <attribute '__dict__' of 'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, '__doc__': None}
'''

#? This is actually a mapping proxy, not an object.
#* This is a read-only, dictionary like structure that ensures that the look-up keys are always strings. 