# my_file = open('scrimba_python/greeting.txt', 'r') # w a 
# print(my_file.read())
# print(my_file.read(15)) # read 15 characters 
# print(my_file.readline()) # read line by line 1
# print(my_file.readline()) # read line by line 2

# line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines()
# print('readlines: ',line_by_line)
# print('splitlines: ',line_by_line1)
# #! always close file 
# my_file.close()

# with open('scrimba_python/friends.csv', 'r') as f:
#     print(f.read())

with open('scrimba_python/friends.csv', 'r') as f:
    # print(f.read())
    friends = f.read().splitlines()
    print(friends)
    # ['John, 1939', 'Eric, 1943', 'Michael, 1943', 'Graham, 1941', 'TerryG, 1940', 'TerryJ, 1942']
    for friend in friends:
        ind_friend = friend.split(',')
        print(ind_friend) #* ['John', ' 1939']
        name = ind_friend[0]
        year = int(ind_friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')

    
    with open('scrimba_python/movies.txt', 'r') as f:
        for line in f:
            print(line)