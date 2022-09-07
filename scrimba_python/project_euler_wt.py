#project Euler #4 - largest palindrome of two 3 - digit numbers 
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099

import time

def is_palindrome(val):
    # cannot slice number, convert to str
    val = str(val)
    # does val == val backwards
    if val == val[::-1]:
        return(True)
    else:
        return(False)
#def is_palindrome(val):
 #   return str(val) == str(val)[::-1]