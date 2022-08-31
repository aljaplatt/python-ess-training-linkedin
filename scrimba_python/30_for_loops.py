
#? 1
#  for letter in 'Norwegian blue':
#     print(letter)

# print("For Loop done!")

#? 2
# for furgle in range(8):
#     print(furgle)

# print("For Loop done!")

#? 3
# for furgle in range(2,8):
#     print(furgle)

# print("For Loop done!")

#* 4 steps
# for furgle in range(1,15,3):
#     print(furgle)

# print("For Loop done!")

#? 5
# for furgle in ['John','Terry','Eric','Michael','George']:
#     print(furgle)

# print("For Loop done!")

##? 6
# friends = ['John','Terry','Eric','Michael','George']
# for index in range(len(friends)):
#    print(friends[index])

# print("For Loop done!")

#? 7

friends = ['John','Terry','Eric','Michael','George']

for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        # break
        continue
    print(friend)

print("For Loop done!")

#? 8 

friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!") 
