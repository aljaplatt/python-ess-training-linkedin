import random 
print('Randomness')

# random num between 0 0.9999999
print(random.random())

# 5 random nums
for i in range(5):
    print(random.random() * 6)


for i in range(5):
    print(random.uniform(1,6))

for i in range(5):
    print(random.randint(1,6))

# odd
for i in range(5):
    print(random.randrange(1,100,2))

# even
for i in range(5):
    print(random.randrange(2,100,2))

# random item from list
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

print(random.choice(friends_list))
# print(random.choices(friends_list)) 
print(random.sample(friends_list, 3)) # multiple - no duplicates

random.shuffle(friends_list)
print(friends_list)

import random, string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
# can specify lower uppercase 

word = ''
for i in range(7):
    word += random.choice(letters_numbers)

word1 = ''.join(random.sample(letters_numbers,7))  #? no duplicates

word = random.choices(letters_numbers, k=7) 
print(word)
print(word1)