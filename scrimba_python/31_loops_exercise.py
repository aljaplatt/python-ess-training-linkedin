names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)
print(names)

for _ in range(2):
    name = input('Invite someone: ')
    names.append(name)

print(names)

for name in names:
    print(f'{name.title()}, you are invited to the party')


# scrimba solution:

# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# msg = 'You are invited to the party on saturday.'
# #names.extend(names1)
# names += names1
# for index in range(2):
#     names.append(input('Enter a new name: '))

# for name in names:
#     #msg1 = f'{name.title()}! {msg}'
#     msg1 = name.title() + '! ' + msg
#     print(msg1)