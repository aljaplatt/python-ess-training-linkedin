
#Choosing a random number between 1 and 100.
# import random 
from random import randint

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        
    elif guess < answer:
        print("Too low.")
        
    else:
        print(f"You got it! The answer was {answer}.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# answer is a random num between and inc 1 & 100
answer = randint(1, 100)


  #Make function to set difficulty.

#Let the user guess a number.
guess = int(input("Make a guess: "))

#Function to check user's guess against actual answer.

#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.
