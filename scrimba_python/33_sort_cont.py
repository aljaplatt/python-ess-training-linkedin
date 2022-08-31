my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list)) #* [-3, -2, 1, 5, 7]
print(sorted(my_list, key = abs)) #* [1, -2, -3, 5, 7]

print(sorted(my_llist)) #* [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]

print(sorted(my_llist, key = lambda item :item[0] ))
print(sorted(my_llist, key = lambda item :item[1] ))
print(sorted(my_llist, key = lambda item :item[2]))
