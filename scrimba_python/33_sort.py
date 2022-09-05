print('sort() and sorted()')
print('Immutability and return values')

my_list = [1,5,3,7,2] # mutable - have sorting method
my_dict = {'car':4,'dog':2,'add':3,'bee':1} #???
my_tuple = ('d','c','e','a','b') # immutable - no sort, have to typecast
my_string = 'python'  # immutable - no sort, have to typecast

#* LISTS
#? Sort doesnt actually return anything - just does the work

# print(my_list,'original')
# print(my_list.sort()) #? None, doesn't return anything
# my_list.sort()
# print(my_list, 'sort') #* [1, 2, 3, 5, 7] 
# # print(my_list.reverse()) #? None, doesn't return anything
# # my_list.reverse() #? None, doesn't return anything
# # # my_list.reverse()
# # print(my_list, 'reverse')
# print(my_list,'original')
# print(my_list.reverse())
# print(my_list,'new')

# print(sorted(my_list), 'sorted')

#TODO - sorted(my_list) - is the same as doing - my_list1 =sorted(my_list)
#todo, returns a new list 

print('RESEVERSED OBJ', reversed(my_list))
print('RESEVERSED OBJ', list(reversed(my_list)))

print(my_list[::-1])

#* TUPLES

# print(my_tuple,'original') #* ('d', 'c', 'e', 'a', 'b') original
# print(sorted(my_tuple)) #* ['a', 'b', 'c', 'd', 'e'] #? LIST
# print(my_tuple,'new') #* ('d', 'c', 'e', 'a', 'b') new

#* DICTS - SORTS KEY VALUES

print(my_dict,'original') #* {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
print(sorted(my_dict)) #* ['add', 'bee', 'car', 'dog']
print(my_dict,'new') #* {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new
print(sorted(my_dict.items())) #* [('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]
print(sorted(my_dict.values())) #* [1, 2, 3, 4]
print(sorted(my_dict.values(), reverse=True))