class MercedesBenz:
    pass


print(MercedesBenz) # <class '__main__.MercedesBenz'>
print(type(MercedesBenz)) # <class 'type'>
print(MercedesBenz.__bases__) # (<class 'object'>,) - root object for all classes in python
print(MercedesBenz.__name__) # MercedesBenz

m1 = MercedesBenz()
m2 = MercedesBenz()

print(m1 == m2 ) # False - different objects, in memory 
print(m1 == m1 ) # True