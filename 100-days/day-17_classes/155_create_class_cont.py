# Set attributes in constructor

class Car:
    def __init__(self, seats):
        self.seats = seats


my_car = Car(5)
print(my_car.seats) #* 5

#* Self is the object that is being created/initialised 
#* seats is a parameter that needs to be passed in when an object gets constructed from this class 

class User:
    def __init__(self, user_id, username):
        #* Initialise attributes 
        print('Init function called')
        self.id = user_id
        self.username = username
        #? default value, doesn't make sense to pass in 0 every time. 
        self.followers = 0 

user_1 = User('001', 'Alex')
user_2 = User('002', 'Angelo') #! will err if args are not provided 

print(user_1.username)
print(user_2.username)