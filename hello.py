from termcolor import colored


print(colored('hello world', 'green', attrs=['bold', 'reverse']))

x = 5

print(x)

# cannot start with number
x1 = x + 1
print(x1)

name = 'alex'
print(type(name)) # str, int, float 

print('Alex ' + 'Platt')
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

#* Dictionaries -  like an object ? - unique keys 

my_dictionary = {
    'apple': 'a red fruit',
    'bear': 'hairy animal',
    'apple': 'sometimes green fruit'
}

print(my_dictionary['apple']) #* will pick last one - 'apple': 'sometimes green fruit'

#* Operators 

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