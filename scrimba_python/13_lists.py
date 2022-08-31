friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
new_friends = friends[:]

# print(friends)
# print(friends[1],friends[4])
# print(friends[-1])
# print(friends[2:4])
# print(friends[:4])
# print(len(friends))
# print(friends.index('Eric'))
# print(friends.count('Eric'))

friends.sort() # alphabetically / ascending
cars.sort() # alphabetically / ascending
# print(friends)
# print(cars)
# friends.sort(reverse=True) 
# friends.reverse()
# print(friends)

# print(min(cars)) #* 130
# print(max(cars)) #* 911
# print(sum(cars)) #* 2952
# print(min(friends)) #* eric

# friends.append('TerryG')
# friends.insert(0, 'TerryG')
# print(friends)
# friends[2]='TerryG'
friends.extend(cars)
# friends.remove('Eric')
# friends.pop()
# friends.pop(2)
# friends.pop(-1)
# friends.clear() #* empty list
# del friends[2]
print(friends)

# new_friends = friends[:]
# new_friends = friends.copy()
# new_friends = list(friends)
# print(new_friends)