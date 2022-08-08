from os import pread


user_iq = 190 #* snake case

print(user_iq)

#* dunders should be left alone 

#? Expressions vs statements

iq = 100
#*  .      Expression produces a value
user_age = iq / 5 
#? the whole thing is a statement 

#? Augmented assignment operator 

some_value = 5
some_value = 5 + 2 #* 7
some_value = some_value + 2 #* 7
some_value += 2 #* 7

some_text = 'Alex'

some_text += 'Platt'

print(some_text) #* AlexPlatt

for _ in range(2):
    some_text += 'James'
    some_text += 'Platt'

print(some_text) #* AlexPlattJamesPlattJamesPlatt

def write_lines():
    for _ in range(5):
        # print('All work and no play makes Jack a dull boy \n')
        print('All work and no play makes Jack a dull boy')

write_lines()

#? 

write_lines = 0

while write_lines < 10:
    print('Yippee Ki yay')
    write_lines += 1