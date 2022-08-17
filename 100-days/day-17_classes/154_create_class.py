#Class keyword followed by the name of your class
# class Car: 

# class User:
#     pass

class User:
    def __init__(self):
        #* Initialise attributes 
        print('Init function called')
    

#? New object user_1 created from the User class 
user_1 = User()

#! this will create an attributes but is long, repetitive, err prone 
user_1.id = '001'
user_1.username = 'Bono'
print(user_1.username)

user_2 = User()

user_2.id = '002'
user_2.username = 'Bon Jovi'

print(user_2.username)

#? We can do this once as part of the class using a constructor
#? The constructor is part of the blueprint that allows us to specify what should happen when our object is being constructed - AKA initialising an object
#* When an object is being initialised - we can set variables to their starting values 

#TODO: in python we create the constructor by defining a special function - the init function - line 8/9

# class User:
#     def __init__(self):
#         #* Initialise attributes 

#* the init function is called every time a new object is created from this class 
