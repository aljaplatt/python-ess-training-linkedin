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