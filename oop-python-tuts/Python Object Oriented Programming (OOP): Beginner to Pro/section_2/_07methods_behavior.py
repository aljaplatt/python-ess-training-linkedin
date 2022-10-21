# better to have class state consolidated within the class definition 
# class MercedesBenz:
#     doors = 2
#     wheels = 4
#     model = "G"


# def drive():
#     return "A car is being driven"

# print(drive())

class MercedesBenz:
    doors = 2
    wheels = 4
    model = "G"

    #* self represents the instance to which the method belongs.
    #? self is not MercedesBenz, it is m1, or m2 or whatever the instance is that you're using
    def drive(self):
        #! return the instance itself 
        return self 

m1 = MercedesBenz()
m2 = MercedesBenz()

print("PRINT: ", m1.drive) #! <bound method MercedesBenz.drive of <__main__.MercedesBenz object at 0x104ae2740>>

print(m1 == m1.drive()) #! True
print(m1 is m1.drive()) #! True

# tracing drive 

print("TRACE CLASS: ",MercedesBenz.drive) # <function MercedesBenz.drive at 0x1022c7880>
print("TRACE INSTANCE 1: ",m1.drive) # <bound method MercedesBenz.drive of <__main__.MercedesBenz object at 0x1025c6770>>
print("TRACE INSTANCE 2: ",m2.drive) # <bound method MercedesBenz.drive of <__main__.MercedesBenz object at 0x100ea2740>>

print(type(MercedesBenz.drive)) # <class 'function'>
print(type(m2.drive)) # <class 'method'> - function bound to an instance of a class 

#? 1. we add behaviour to our classes by defining functions 
#? 2. These functions always have at least one parameter - self 
#? 3. When functions are defined within the body of a class, they become bound to instances of that class  