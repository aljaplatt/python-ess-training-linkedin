
#* Calculator

def add(n1, n2) :
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 

num1 = int(input('Pick number 1: '))

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num2 = int(input('Pick number 2: '))

#? will print out the key only  
for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation from the line above: ')
calculation_func = operations[operation_symbol]

answer = calculation_func(num1, num2)



print(f"{num1}{operation_symbol} {num2} = {answer}")