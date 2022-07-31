
#* Calculator

def add(n1, n2) :
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# num1 = int(input('Pick number 1: '))
# num2 = int(input('Pick number 2: '))

#? will print out the key only  
for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation from the line above: ')