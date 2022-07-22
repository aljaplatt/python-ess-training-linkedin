#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

#* 3 ways: 
# for letter in chosen_word:
#     display.append('_')

# for _ in chosen_word:
#     display.append('_')

for _ in range(len(chosen_word)):
    display += '_'

print(display)


guess = input("Guess a letter: ").lower()


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

#* we have to change to above for loop to one that uses range() so we can get the position of the letter.

#? range between 0 and length of chosen word. 
#* for each of those letters the for loop is going to give us a number, or position to work with.
#? first iteration, position = 0
#? second iteration, position = 1 etc 
for position in range(len(chosen_word)):
#* How can we get the current letter in chosen word. - given that we know the position?
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)
