from termcolor import colored
from decimal import Decimal, getcontext
import math
from collections import defaultdict
from datetime import datetime

print(colored('hello world', 'green', attrs=['bold', 'reverse']))

x = 5

print(x)

# cannot start with number
x1 = x + 1
print(x1)

name = 'alex'
print(type(name)) # str, int, float 

print('Hello World \nHello World') 

print('Alex ' + 'Platt')
print('Hello ' + name)
print('1' + '1') # 11
# print('1' + 1) # Type err 

# Boolean - True False 

print(1 == 1) # True 
print(1 == 2) # False  

#* Data structures

my_list = [1, 'alex', [2,3]]

print(len(my_list)) # length 3 

#* Sets - similar to a list - all elements have to be unique 

my_set = {1,2,3,4,5}
print(my_set)

#? order in sets doesnt matter 
{1,2} == {2, 1}

#* Tuples -  can't append or add things to tuples, good for fixed values, less memory required 

my_tuples = (1,2,3)

# my_tuples.append(4) #! ERR - Tuple has no append attribute
#* Dictionaries -  like an object ? - unique keys 

my_dictionary = {
    'apple': 'a red fruit',
    'bear': 'hairy animal',
    'apple': 'sometimes green fruit'
}

print(my_dictionary['apple']) #* will pick last one - 'apple': 'sometimes green fruit'

#* Operators 

print('QUESTION:', 456 % 10 ) #? 6

#? Division will give a decimal or float back 

# You can do string multiplication
print('-- string 1 -- ' * 4)

#* Logical operator 

True and True
True and False
True or False 
not True
not False 

1 in [1,2,3,4,5] #* True
10 in [1,2,3,4,5] #* False 
10 not in [1,2,3,4,5] #* True 

print('Cat' in 'I prefer A dog to a Cat') #* True 
print('Cat' not in 'I prefer A dog to a Cat') #* False 

#* Control Flow
# if block needs indentation - colon followed by indent 
a = True 
b = True
c = True
if a: 
    print('a is true')
    print('also this')
    if b: 
        print('both are true')
        if c: 
            print('all are true')
else: 
    print('It is false')
print('Always print this')

#? LOOPS

a = [1,2,3,4,5]
for num in a:
    print(num)

z = 0
while z < 5:
    print(z)
    z = z + 1

#* FUNCTIONS

def multiplyByThree(val):
    return 3 * val 

multiplyByThree(4)

def multiply(val1, val2): 
    return val1 * val2

multiply(3, 4)

lst = [1,2,3]

def appendFour(myList):
    myList.append(4)

appendFour(lst)
print(lst)

type(None)

#! Classes and Objects 
#? The init function is a special python defined function, that is called whenever an instance of the class Dog is created. 
#* self is the specific instance of the Dog class, after we've initialised it. 
class Dog:
    # def __init__(self):
    #     self.name = 'Rover'
    #     self.legs = 4
    def __init__(self, name):
        self.name = name
        self.legs = 4
    
    def speak(self): 
        print(self.name + ' says: Bark!')
    # def speak(self):
    #     print('Bark!')

#? my_dog is equal to a newly created instance of the Dog class
my_dog = Dog('Rover')
another_dog = Dog('Guts')

my_dog.speak() #? 'Rover says: Bark!' 
another_dog.speak() #? 'Guts says: Bark!' 

print(type(Dog('Rover')))

#? Ints and Floats

print(20 / 4)
print( 4 + 4.0)
print(4 * 4.0)
print(4 ** 4.0) #? 256.0
print(int(4 ** 4.0)) #? 256 - int is a built in class in python 
print(int(8.9)) #? 8
print(int(8.9999)) #? 8 
print(int(14/3)) #? 4
print(round(14/3)) #? 5
print(round(14/3, 2)) #? 4.67 - 2 dec places

print(1.2 - 1.0) #? 0.19999999996 - Floating point err
print(round(1.2 - 1.0, 2)) #? 0.2

print(int('100')) #* will print number, not string 

#? Bases 

print(int('1ab', 16)) #* 427

#? Import Class Decimal and function getcontext from decimal module at the top 

getcontext() #* returns a context object, with global settings that are applied to the Decimal class.  prec=28

getcontext().prec=4

getcontext() #? prec=4

Decimal(1) / Decimal(3) #? '0.3333' - 4 places

Decimal('3.14') #todo SHORT
#! vs 
Decimal(3.14) #todo LONG

round(1.2 - 1.0, 2)

#* BOOLEANS

print(bool(1)) #? True  
print(bool(0)) #? False - only 'number' that is false 
print(bool('True')) #? True 
print(bool('')) #? False - empty string is false
print(bool([])) #? False 
print(bool([1,2])) #? True 
print(bool({})) #? False 
print(bool(None)) #? False 

myList = [1,2]
if myList:
    print('myList has some values in it')

#? 0 = false - a -b is not true, wont't print
a = 5
b = 5
if a - b:
    print('a and b are not equal')

print(a == b) #? True 

weatherIsNice = True
haveUmbrella = False

# if not haveUmbrella or weatherIsNice:
#     print('Stay in')
# else: 
#     print('Walkies')

#! Python evaluates left to right - the logic above won't act how we want it to.
#? Instead we can write... (   )

# if not (haveUmbrella or weatherIsNice):
#     print('Stay in')
# else: 
#     print('Walkies') 

#todo OR

# if not haveUmbrella and not weatherIsNice:
#     print('Stay in')
# else: 
#     print('Walkies')

if haveUmbrella or weatherIsNice:
    print('Walkies')
else:
    print('Stay in')


#? STRINGS 
#? Slicing 
tvShow = 'The Sopranos'

print(tvShow[0]) #? 'T'
print(tvShow[1]) #? 'h'
print(tvShow[3: 12]) #? ' Sopranos'
print(tvShow[:12]) #? 'The Sopranos'
print(tvShow[5:]) #? from to the end

theList = [1,2,3,4,5]
print(theList[2:4]) #? 3,4
newList = theList[2:4]
print(newList)
print(newList == theList)
print(len(tvShow))
print(len(theList))

#* FORMATTING ~ like template literals - f strings 

print('My number is: ' +str(5))
print(f'My number is: {5}. 5 times 2 is {5*2}') 

print(f'Pi is: {math.pi:.2f}') #? Pi is: 3.14

newLineStr = ''' 
i can now write over mutliple
lines
cool using \'\'\'
'''

print(newLineStr)

#* BYTES obj

print(bytes(4))

#* 4. BASIC DATA STRUCTURES 

#? List slicing 

aList = [1,2,3,4,5]
aList[3:] #? 4,5

aList[0:6:2] #?  1,3,5 - step size of 2 = every other item
aList[::2] #? the same as above 

for i in range(100):
    print(i)
#? 0-99 

aList = list(range(100)) #? arr 0-99
print(aList[::10]) #? - 0, 10, 20, 30 ....
aList[::-1] #? the list backwards 

#? MODIFYING LISTS  

zList = [1,2,3,4]
zList.append(5)
print('append zList with 5:', zList)

zList.insert(3, 'new value')
print('insert:',zList)
zList.remove('new value')
print('remove:',zList)
zList.pop()

while len(zList): #? this will evaluate to false at 0
    print(zList.pop())

print(zList)

a = [1,2,3,4,5]
# b = a
# a.append(6)
print(b) #* [1,2,3,4,5, 6] - points to same location as a in memory - use copy()
b = a.copy()
a.append(6)
print(b) #* [1,2,3,4,5]

#* Sets & Tuples 

aSet = {'a', 'b', 'c'} 
print(aSet)

#? A good way to remove duplicates from a list is to convert list to set, sets can only contain unique values. Then convert back again.

duplicateList = [1,2,3,3,4,4,4,5,5,5,6,6,6,7]
duplicateList = list(set(duplicateList))
print(duplicateList)

#* Order doesn't matter with sets  
#? Declared with { }
#* Order may not be the same when duplicated, but items will be unique
#! - you cannot fetch items by their index   mySet[0] 

aSet.add('d')
print(aSet)

print('a' in aSet) 

aSet.discard('a') #? remove item from set 
print(aSet)

#* order does matter with tuples  
#* cannot modify 
myTuple = ('a', 'b', 'c')
print(myTuple[0]) #? a
#! myTuple[0] = 'z'  - DOESN'T WORK 

#? Memory efficient - can set exact memory requirement 

#? Dictionaries

animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat'
} 

print(animals)
print(animals['a'])
animals['d'] = 'dinosaur'
print(animals['d'])
animals['a'] = 'ant eater'

print(animals.keys()) #? dict_keys(['a', 'b', 'c', 'd'])
print(animals.values()) #? dict_values(['ant eater', 'bear', 'cat', 'dinosaur'})

#? Check for key e, 2nd arg is a default  
animals.get('e', 'elephant')

print(len(animals))

funimals = {
    'a': ['aardvark', 'alien'],
    'b': ['bear', 'beaver'],
    'c': 'cat'
} 

funimals['b'].append('bison')

print(funimals)

funimals['d'] = ['duck']

if 'e' not in funimals:
    funimals['e'] = []
    
funimals['e'].append('eagle')

print(funimals)

#* Default dict

cheese = defaultdict(list)
print(cheese) 

cheese['strong'].append('stilton')
print(cheese) 
cheese['mature'].append('cheddar')
print(cheese) 

#? List comprehensions 

myList2 = [1,2,3,4,5] 
print([2*item for item in myList2]) #* will double everything in the list 

list99 = list(range(100))
filteredList = [item for item in list99 if item % 10 == 0]
print(filteredList) #* all nums divisible by 10

filteredList2 = [item for item in list99 if item % 10 < 3]
print(filteredList2) #* all nums divisible by 10

aString = 'My name is Alex and im stuck in a chair'
print(aString.split('and')) 
print(aString.split()) #* WORDS

def cleanWord(word): 
    return word.replace('a', 'X').lower()

print([cleanWord(word) for word in aString.split()])
print([cleanWord(word) for word in aString.split() if len(cleanWord(word)) > 3])

#* NESTED LIST COMPREHENSIONS

print([[cleanWord(word) for word in sentence.split()] for sentence in aString.split('and')])

#? [['my', 'nxme', 'is', 'alex'], ['im', 'stuck', 'in', 'x', 'chxir']]

#? DICTIONARY COMPREHENSIONS

animalList = [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
animals = {item[0]: item[1] for item in animalList}
print(animals) #? {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
#! SAME 
animals = {key: value for key, value in animalList}
print(animals) #? {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

animals.items() 
#? RETURNS - dict_items([('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')])

list(animals.items())
#? RETURNS - [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]

[{'letter': key, 'name': value} for key, value in animals.items()]


#? RETURNS - [{'letter': 'a', 'name': 'aardvark'},
#  {'letter': 'b', 'name': 'bear'},
#  {'letter': 'c', 'name': 'cat'},
#  {'letter': 'd', 'name': 'dog'}]


#? CONTROL FLOW

#? FIZZBUZZ

# for n in range(1, 101):
#     if n % 15 == 0:
#         print('FizzBuzz')
#     else: 
#         if n % 3 == 0: 
#             print('Fizz') 
#         else: 
#             if n % 5 == 0:
#                 print('Buzz')
#             else:
#                 print(n)

#* ELIF STATEMENTS

for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0: 
        print('Fizz') 
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

x = 5 
print('Fizz' if x % 3 == 0 else x)

#? TERNARY OPERATOR 
# fizzBuzz = 'Fizz' if n % 3 == 0 else n

# fizzBuzz = 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n 

fizzBuzz = 'FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n 

['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in range(1, 101)]

#* Get current date / time 
print(datetime.now())
print(datetime.now().second)

#* WHILE LOOP - WAIT FOR 2 SEC AND PRINT MESSAGE  

wait_until = datetime.now().second + 2

# while datetime.now().second != wait_until:
#     print('Waiting')

# print(f'We are at {wait_until} seconds!')

#? PASS STATEMENT

while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds!')

#? FOR LOOP

theList = [1,2,3,4,5]

for item in theList:
    print(item)


animalLookup = {
    'a': ['avocado', 'avalanche'],
    'b': ['beaver', 'bear grills'],
    'c': ['cucumber'],
    'd': ['dr dre'],
}

for letter, animals in animalLookup.items():
    pass

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'One animal: {animals[0]}')

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'One animal: {animals[0]}')
        break

for number in range(2, 100):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
        else:
            print(f'{number} is prime!')


for number in range(2, 100):
    found_factors = False
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            found_factors = True
            break
    if not found_factors:
        print(f'{number} is prime!')
             

#? CHAPTER 5 QUIZ 
#*1 
for number in range(1, 100):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')

#*2

print(['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)])

#*3

#? If the current number of seconds is 59 seconds, how long will this program run? 
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')

#* 4 - Will the print statement be reached in this code?

for number in range(1, 9):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')