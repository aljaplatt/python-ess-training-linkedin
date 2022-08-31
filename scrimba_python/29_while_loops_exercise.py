print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

import random 

random_num = random.randint(1, 100)
print('RANDOM NUM: ', random_num)
num_of_guesses = 5

while num_of_guesses:
    if num_of_guesses:
        guess = int(input('Guess a number between 1-100: '))
        print('GUESS: ', guess)
        print('RANDOM NUM: ', random_num)

        if guess == random_num:
            num_of_guesses = 0
            print('CORRECT')
        elif guess > random_num:
            num_of_guesses -= 1
            if num_of_guesses:
                print(f'Too high. You have {num_of_guesses} guesses left.')
            else:
                print(f'Unlucky, the correct number was {random_num}')
        elif guess < random_num:
            num_of_guesses -= 1
            if num_of_guesses:
                print(f'Too low. You have {num_of_guesses} guesses left.')
            else:
                print(f'Unlucky, the correct number was {random_num}')
    # else:
    #     print(f'Unlucky, the correct number was {random_num}')

# scrimba answer

# num = 76
# guess = 0
# guess_limit=5
# guess_number = 0
# guess = int(input(f'Guess a number 1-100: '))
# guess_number +=1
# while guess_number < guess_limit:
    
#     if guess != num:
#         guess_number +=1
#         if guess > num:
#             guess = int(input(f'{guess} Too high - Guess again 1-100: '))
#         else:
#             guess = int(input(f'{guess} too low - Guess again 1-100: '))
#     if guess == num:
#         print(f'You Win! You Guessed it: {guess}')
#         break
    
# if guess != num:
#     print(f'Sorry you lose! It was {num}')
