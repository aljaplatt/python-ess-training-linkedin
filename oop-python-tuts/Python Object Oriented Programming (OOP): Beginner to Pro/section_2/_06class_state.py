
# These attributes live in the class namespace
class MercedesBenz:
    doors = 2
    wheels = 4

#* class state is stored in a mappingproxy object and retrieved using __dict__
# class dictionary accessible under __dict__
print(MercedesBenz.__dict__)
print(type(MercedesBenz.__dict__)) # <class 'mappingproxy'>
'''
{'__module__': '__main__', 'doors': 2, 'wheels': 4, '__dict__': <attribute '__dict__' of 'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, '__doc__': None}
'''

#* class state is shared and accessible by all instances of that class

MercedesBenz.model = "G"
m3 = MercedesBenz()
print(m3.model) # G