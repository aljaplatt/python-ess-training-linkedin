from art import logo, vs
from game_data import data
import random 

def format_data(acc):
    '''
    #* Returns account data in printable form 
    '''
    #? format account data into printable format
    account_name = acc['name']
    account_desc = acc['description']
    account_country = acc['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# ? Display art  
print(logo)
score = 0
continue_game = True

while continue_game:
    #* generate random account from the game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"against B: {format_data(account_b)}")

    #* ask user for a guess A or B?
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #? Check if user is correct  
    #* get follower count of each acc
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #? use if statement to check if user is correct - def check_answer 

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #* give user feedback on their guess 
    if is_correct:
        score += 1
        print(f"You're correct!. Current score {score}") 
    else: 
        continue_game = False
        print(f"Nope. Final score {score}")

    #? score keeping

    #* make game repeatable  

    #? making accounts at position b, move to position a 

    #* Clear terminal between rounds     