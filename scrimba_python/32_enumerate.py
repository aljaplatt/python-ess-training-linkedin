print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']


# i = 1
# for friend in friends:
#     print(i, friend)
#     i = i +1 # += 1

# for num, friend in enumerate(friends,1):
#     print(num, friend)

# 51 = starting num 
for num, friend in enumerate(friends,51):
    print(num, friend)

#? efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

print(type(enumerate(friends))) #? <class 'enumerate'>
print(list(enumerate(friends))) #? [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta'), (4, 'Colin')]


