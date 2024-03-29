

#Choosing a random number between 1 and 100.
# import random 
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
#Make function to set difficulty.
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # answer is a random num between and inc 1 & 100
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 


    turns = set_difficulty()
    
    guess = 0
    # Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess a number.
        guess = int(input("Make a guess: "))

#Function to check user's guess against actual answer.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('Game over')
            return 

#todo Track the number of turns and reduce by 1 if they get it wrong.

game ()
