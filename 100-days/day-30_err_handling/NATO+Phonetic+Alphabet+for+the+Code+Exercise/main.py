# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# word = input("Enter a word: ").upper()
# # #? this is the line where we check the letters from the users word against the dictionary.
# # output_list = [phonetic_dict[letter] for letter in word]
# try:
#     output_list = [phonetic_dict[letter] for letter in word]
# except KeyError:
#     print("Sorry only letters allowed")
# print(output_list)

# if we want this to repeat, best to put it in function 

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters allowed")
        generate_phonetic()
    else:
        print(output_list)
