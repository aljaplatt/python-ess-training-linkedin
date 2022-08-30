#Sets - blazingly fast unordered Lists - no duplicates
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
# ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends_tuple)
# ('John', 'Michael', 'Terry', 'Eric', 'Graham')
print(friends_set)
# {'Graham', 'Eric', 'John', 'Terry', 'Michael'}

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set)) #? Which are in both? 
# {'Graham', 'Eric'}
print(friends_set.difference(my_friends_set)) #? which are different?
# {'John', 'Terry', 'Michael'}
print(friends_set.union(my_friends_set)) #? combine with no duplicates?
# {'Eric', 'Terry', 'Loretta', 'John', 'Graham', 'Reg', 'Colin', 'Michael'}

#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()

