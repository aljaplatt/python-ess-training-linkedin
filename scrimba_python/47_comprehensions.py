print('Comprehensions')

numbers = [1,2,3,4,5,6,7,8,9]  

#? give me a list with num squared for each num in numbers
# new_list = []
# for num in numbers:
#     new_list.append(num*num)
# print(new_list)

#* Same as:

# new_list = [num*num for num in numbers]
# print(new_list) 

#? give me a list with num for each num in numbers if num is even 
# new_list = [num for num in numbers if num % 2 == 0]
# print(new_list) #* [2, 4, 6, 8]

#? give me a list of odd nums 
# new_list = [num for num in numbers if num % 2 == 1]
new_list = [num for num in numbers if num % 2 != 0] #? same
print(new_list) #* [1, 3, 5, 7, 9]


#* Using lambda & filter 
#*                                        ?? -> apply it to numbers
new_list = filter(lambda num: num % 2 ==0,numbers)
print(list(new_list)) #* [2, 4, 6, 8]

#? I want a (letter, num) pair for each letter in 'spam' and each number in '0123'

#* using for loop

# new_list = []
# for letter in 'spam':
#    for num in range(4):
#        new_list.append((letter,num))
# print(new_list)

#* Same as:

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)