# combine different iterables

from math import comb


# nums = [1,2,3,4] 
nums = '1234'
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

# combo = zip(nums, letters)
# print(combo) #? <zip object at 0x1031abb00> cannot see inside
# #* can turn into dictionary
# #?  combo = dict(zip(nums,letters))
# #* {'1': 'a', '2': 'b', '3': 'c', '4': 'd'} 

# print(list(combo)) #? turn into a list -> [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# #? list of tuples matched by index number  
# #* would still work with string? - yes, nums now string though -> [('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd')]

#? can turn into dictionary
#  combo = dict(zip(nums,letters))

#todo -> can use more than one iterable

nums = '1234' 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
combo = list(zip(nums,letters,names))
# print(combo) #* [('1', 'a', 'John'), ('2', 'b', 'Eric'), ('3', 'c', 'Michael'), ('4', 'd', 'Graham')]

#? Unzipping / unpacking

num,let,nam =zip(*combo)
# print(num,let,nam)



keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

keys = keys.split()
values = values.split()
# print(keys,values)
#* ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden'] 

en_sv_dict = dict(zip(keys,values))
# print(en_sv_dict)
# {
#     'this': 'denna', 
#     'parrot': 'papegojan', 
#     'is': 'är', 
#     'deceased': 'avliden'
# }

#* Dictionary comprehension 

new_dict = {key:value for key,value in zip(keys,values)}
# print(new_dict)
# same result as above 

#* Take dictionary apart - return to lists

en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print(en,sv) #? ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

#todo -> does the same but returns tuples
en1,sv1 = zip(*en_sv_dict.items())
print(en1,sv1)


