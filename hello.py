from termcolor import colored
from decimal import Decimal, getcontext
import math

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