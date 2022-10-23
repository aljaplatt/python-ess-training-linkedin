from string import ascii_letters, punctuation
from copy import copy
from random import choices


INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

population = copy(INPUT_UNIVERSE["letters"])
# print(population)
'''
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
'''

password_arr = choices(population, k=5)
print(password_arr) # ['A', 'Q', 'T', 'N', 'o']

password_str = "".join(password_arr)
print(password_str) # AQTNo

