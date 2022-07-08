
#* Data types

#? Numbers

print(1_000_000_000) 

#! len(12345) -  TypeErr

num_char = len(input('enter name: \n'))
# print('your name has ' + num_char + ' characters') #! - TypeErr cannot concaternate int
#? TYPE CHECKING 
print(type(num_char))

#? TYPE CONVERSION/CASTING 

new_num_char = str(num_char)
print('your name has ' + new_num_char + ' characters') 

print(int('70') + float('100.5'))
print(str(70) + str(100))