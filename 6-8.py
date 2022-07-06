import math, time
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

#? CHAPTER 7 - CLASSES AND OBJECTS

# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.legs = 4
    
#     def speak(self):
#         print(self.name + ' says: Bark!')

# myDog = Dog('Rover')
# print(myDog.name)
# print(myDog.legs)

#* name and legs are instance attributes 

#? Static attributes - class name - orientation or class instance, self 
#? Static methods - we cannot do this - DECORATOR?! @staticmethod

#* INHERITANCE - A CHILD CLASS CAN EXTEND A PARENT CLASS.
class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')
    
    def getLegs(self):
        return self._legs


class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')
        
    def wagTail(self):
        print('Vigorous wagging!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()

myDog = Dog('Rover')
myDog.speak()

#? EXTENDING BUILT-IN CLASSES 

myList = list()

# class UniqueList(list):
#     def append(self, item):
#         if item in self:
#             return
#         super().append(item)
        
# uniqueList = UniqueList()
# uniqueList.append(1)
# uniqueList.append(1)
# uniqueList.append(2)

# print(uniqueList)

class UniqueList(list):
    
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'
        

    def append(self, item):
        if item in self:
            return
        super().append(item)
        
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)

#* The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class. 

#* The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments.  

#! 8. ERRORS

# def causeError():
#     return 1/0

# causeError() #? ZeroDivisionError: division by zero

# def causeError():
#     return 1/0

# def callCauseError():
#     return causeError()

# callCauseError() 

#* TRY / EXCEPT
#? Catch exception so it doesn't cause an err  

# try: 
#     1/0
# except Exception as e: 
#     print(type(e)) #todo - <class 'ZeroDivisionError'>

# def causeError():
#     try: 
#         return 1/0
#     except Exception as e: 
#         return e #todo - <class 'ZeroDivisionError'>

# causeError()

#? HANDLING EXCEPTIONS 

# def causeError():
#     try:
#         return 1/0
#     except Exception:
#         print('There was some sort of error!')
    
# causeError()

#* FINALLY

# def causeError():
#     try:
#         return 1/1
#     except Exception:
#         print('There was some sort of error!')
#     finally:
#         print('This will always execute!')
    
# causeError()

# def causeError():
#     start = time.time()
#     try:
#         time.sleep(0.5)
#         return 1/0
#     except Exception:
#         print('There was some sort of error!')
#     finally:
#         print(f'Function took {time.time() - start} seconds to execute')
    
# causeError()

#* CATCHING ERR BY TYPE

def causeError():
    try:
        return 1 + 'a'

    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception:
        print('There was some sort of error!')

    
causeError()

#?  CUSTOM DECORATORS 

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sort of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()

#? RAISING EXCEPTIONS 

@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)
    
raiseError(1)

#! WRITING FUNCTIONS TO RAISE EXCEPTIONS IS POWERFUL WHEN YOU COMBINE IT WITH CUSTOM EXCEPTIONS

#* CUSTOM EXCEPTIONS

class CustomException(Exception):
    pass


def causeError():
    raise CustomException('You called the causeError function!')
    
causeError()

# CustomException                           Traceback (most recent call last)
# Input In [3], in <module>
#       5 def causeError():
#       6     raise CustomException('You called the causeError function!')
# ----> 8 causeError()

# Input In [3], in causeError()
#       5 def causeError():
# ----> 6     raise CustomException('You called the causeError function!')

# CustomException: You called the causeError function!

#* ADDING ATTRIBUTES

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')
        
class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'
    
class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'
    
def raiseServerError():
    raise ServerError()
    
raiseServerError()

#* WRITING CUSTOM EXCEPTION MESSAGES IS A GREAT WAY TO KEEP CODE CLEAN AND ORGANISED. 