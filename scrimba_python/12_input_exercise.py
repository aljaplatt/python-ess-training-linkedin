# name = input('What is your name?: ')
# distance = input('Distance(km) to convert: ')

# print(f"Hey, {name.capitalize()}. {distance} km is equal to {float(distance) * 0.621371} miles")

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')