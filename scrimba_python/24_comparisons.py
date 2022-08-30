a = 7
b = 3
# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)

# print('o' in 'John')
# print('o' not in 'John')

a = [3,7,42]
b = a
print(a == b) #? True
print(a is b) #? True ? Are they occupying the sam memory space? Yes.
print(id(a), id(b)) #? 4307691008 4307691008 = location in memory 

print(int(True)) #? 1
print(int(False)) #? 0