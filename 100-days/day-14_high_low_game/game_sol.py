from art import logo
from game_data import data
import random 

def format_data(acc):
    #? format account data into printable format
    account_name = acc['name']
    account_desc = acc['description']
    account_country = acc['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


# ? Display art  
print(logo)
#* generate random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")
#* ask user for a guess A or B?

#? Check if user is correct  
#* get follower count of each acc
#? use if statement to check if user is correct   

#* give user feedback on their guess  

#? score keeping

#* make game repeatable  

#? making accounts at position b, move to position a 

#* Clear terminal between rounds     