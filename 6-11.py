import math
#? Functions 

# def performOperation(num1, num2, operation): 
#     if operation == 'sum':
#         return num1 + num2
#     if operation == 'multiply': 
#         return num1 * num2 

# result = performOperation(2,3, 'sum')

# def performOperation(num1, num2, operation='sum'): 
#     if operation == 'sum':
#         return num1 + num2
#     if operation == 'multiply': 
#         return num1 * num2 

# result = performOperation(2,3, operation='multiply')

# print(result)

def performOperation(num1, num2, operation='sum', message='Message'):
    print(message) 
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply': 
        return num1 * num2 

result = performOperation(2,3, message='We can do in this order if we specify the argument', operation='multiply')

print(result)

#* KEYWORD ARGS MUST COME AFTER POSITIONAL ARGS (2,3) 

#* *ARGS - DOESNT WORK WITH KEYWORD ARGUMENTS

# def doFunction(*args):
#     print(args)

# print(doFunction(1,2,3)) #? RETURNS (1,2,3) TUPLE 

#* *KWARGS - DOES WORK WITH KEYWORD ARGUMENTS

def doFunction(*args, **kwargs):
    print(args)
    print(kwargs)

print(doFunction(1,2,3, job='learn python')) #? RETURNS (1,2,3) TUPLE, kwargs comes back as a dictionary 

def spectacularFunction(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)

print(spectacularFunction(1,2,3,4,5,6,7, operation='multiply'))
print(spectacularFunction(1,2,3,4,5,6,7))

#? VARIABLES AND SCOPE 

def localsFunction(*args, operation='sum'):
    print(locals())

print(localsFunction(1,2, operation='multiply'))

#? RETURNS dictionary of all arguments - kw or positional 
#* {'operation': 'multiply', 'args': (1, 2)}

print(globals())

# message = 'Some global data'
# varA = 2
# def function1(varA, varB):
#     message = 'Some local data'
#     print(varA)
#     print(message)
#     print(locals())
    
    
# def function2(varC, varB):
#     print(varA)
#     print(message)
#     print(locals())
    
# function1(1, 2)
# function2(3, 4)

def function1(varA, varB):
    message = 'Some local data'
    print(varA)
    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')
        
    inner_function(123, 456)
    

function1(1, 2) #? 1, inner_function local scope: {'varA': 123, 'varB': 456}

#* FUNCTIONS AS VARIABLES

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
'''

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.', '-', ',', '*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewlines(text):
    text = text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) < 6])


processingFunctions = [lowercase, removePunctuation, removeNewlines]

for func in processingFunctions:
    text = func(text)

print(text)

#* LAMBDA FUNCTION

(lambda x: x + 3)(5)

myList = [5,4,3,2]
print(sorted(myList))

myList = [{'num': 3}, {'num': 2}, {'num': 1}]
sorted(myList, key=lambda x: x['num'])

#? [{'num': 1}, {'num': 2}, {'num': 3}]

