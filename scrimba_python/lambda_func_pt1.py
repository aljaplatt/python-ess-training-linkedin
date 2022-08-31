print(' Lambda Functions')

# def square(x):
#     return x*x
# print(square(3)) #? 9

# def square2(x):return x*x
# print(square2(3))

#name = lambda parameter(s): expression

sq_1 = lambda x: x*x
print(sq_1(3)) #? 9

double_mult = lambda x,y: 2*x*y
print(double_mult(2,3)) #? 12  

def name_and_alias(name,alias):
    return name.strip().title() + ': ' + alias.strip().title()
    
print(name_and_alias(' john  ClEEse  ','HECKLER'))

name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()

print(name_and_alias1(' john  ClEEse  ','HECKLER'))


#########################################################

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

def sort_names(name):
    return name.split(' ')

monty_python.sort(key = lambda name:name.split(' ')) # ordered by first name
print(monty_python)
monty_python.sort(key = lambda name:name.split(' ')[-1]) # ordered by surname
print(monty_python)

monty_python.sort(key= sort_names)
print(monty_python)
