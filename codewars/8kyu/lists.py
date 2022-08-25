
#? Fake Binary
"""
    #* Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

    Note: input will never be an empty string
"""


# Python program to iterate
# over 3 lists using zip function
  
import itertools 
  
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

book_ids_list  = ['83943218-232c-11ed-9a59-beb2bf7533dc', '839576be-232c-11ed-9a59-beb2bf7533dc', '8395bb7e-232c-11ed-9a59-beb2bf7533dc', '8395bb7e-232c-11ed-9a59-beb2bf7533dc']


# iterates over 3 lists and executes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for (a, b, c) in zip(num, color, value):
     print (a, b, c)

