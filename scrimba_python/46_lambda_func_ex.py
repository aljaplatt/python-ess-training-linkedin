print('Lambdas Exercise')

# ? 1
# def f(x): return x + 5
#f = ...#insert equivalent lambda here

f = lambda x: x+5
# print(f(2))

# ? 2
# def strip_spaces(str):
#    return ''.join(str.split(' '))
#write equivalent lambda and insert Lambda here
strip_spaces1 = lambda str: ''.join(str.split())
strip_spaces2 = lambda str: ' '.join(str.split())
print(strip_spaces1('Monty Pythons Flying Circus')) #? MontyPythonsFlyingCircus
print(strip_spaces2('Monty Pythons Flying Circus')) #? Monty Pythons Flying Circus

# string = 'Monty Pythons Flying Circus'

# split_string = string.split()
# print(split_string) #* ['Monty', 'Pythons', 'Flying', 'Circus']
# split_string = string.split('-') 
# print(split_string) #* ['Monty Pythons Flying Circus'] - no dash

#? Join list to string 

# back_to_string = ' '.join(split_string)
# print(back_to_string) #? Monty Pythons Flying Circus

# back_to_string = '-'.join(split_string)
# print(back_to_string) #? Monty-Pythons-Flying-Circus

# back_to_string = ''.join(split_string)
# print(back_to_string) #? MontyPythonsFlyingCircus

# ? 3

def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
#write lambda below 
join_list_no_duplicates1 = lambda list_a,list_b: list(set(list_a + list_b))
# print(join_list_no_duplicates(list_a,list_b))
# print(join_list_no_duplicates1(list_a,list_b))


la = [1,2,3,4]
lb = [3,4,5,6,7]
lc = list(set(la + lb)) 
print('LC: ', lc) #? {1, 2, 3, 4, 5, 6, 7} -> LC:  [1, 2, 3, 4, 5, 6, 7]

# ? 4
#Complete the function so it returns a function
# def create_quad_func(a,b,c):
#    '''return function f(x) = ax^2 + bx + c'''
#    return lambda x:
#f = create_quad_func(2,4,6)
#g = 
#print(f(2))
#print(g(2))

def create_quad_func(a,b,c):
    # a times x to the power of 2 = a*x**2
    # b times x + C = b*x + c

    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c
f = create_quad_func(2,4,6)
# write your own function = just use diff arguments 
g = create_quad_func(1,2,3)
# print(f(2))
# print(g(2))

# ? 5

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# print(sorted(signups)) #* Lexicographic sort ['MPF104', 'MPF17', 'MPF2', 'MPF20', 'MPF3', 'MPF45'] 
#! - puts 104 before 20, because 104 starts with 1 & 20 starts with 2

# sort by integer
#print(sorted(...) # Integer sort
#* here we ignore / slice the first 3 digits, then convert the rest from a string to int.
#? first arg is what we want to sort
#? second is how we want to sort
# print(sorted(signups,key = lambda id:int(id[3:]))) # Integer sort

# ? 6

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]
print(player_list)
#? [<__main__.Player object at 0x1010bfb80>, <__main__.Player object at 0x1010bfb20>, <__main__.Player object at 0x1010bfac0>]


#Exercise: Sort this by score using lambda!
#write code here
player_list.sort(key = lambda playyer: playyer.score, reverse = True)
print('6: ', [player.name for player in player_list])
print('6: ', [player.score for player in player_list])

player_scores = [player.score for player in player_list]
print(player_scores)