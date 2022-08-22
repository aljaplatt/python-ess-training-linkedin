my_tuple = (1,5,23)
print(my_tuple)
# my_tuple[2] = 32 #! TypeError: 'tuple' object does not support item assignment

my_list = list(my_tuple)

print(type(my_list))

my_list[2] = 32

print(my_list)
