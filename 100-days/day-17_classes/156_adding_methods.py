# Set attributes in constructor

class Car:
    def __init__(self, seats): #* constructor function 
        self.seats = seats

    # def enter_race_mode():
    


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
        self.following = 0 
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'Alex')
user_2 = User('002', 'Angelo') #! will err if args are not provided 

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

