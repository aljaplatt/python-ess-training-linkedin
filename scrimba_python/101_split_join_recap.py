print('Welcome to Python 101: Split and Join')

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']

# print(msg.split())

# friends = csv.split(',')
# print(friends) #? ['Eric', 'John', 'Michael', 'Terry', 'Graham']

#* 1. specify what joining char is ' '
#* 2. use join method .join()
#* 3. specify what we want to join 

# friends_str = ' '.join(friends)
# print(friends_str, type(friends_str)) 

# friends_str = ', '.join(friends)
# print(friends_str, type(friends_str)) 


#? Strip whitespace from string 

whitespace ='Welcome  to   Python  101: Split  and Join'
#? 1. split
# print(whitespace.split())  #? ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']

#? 2. join
# print(''.join(whitespace.split()))  #? WelcometoPython101:SplitandJoin

#* OR

# print(whitespace.replace(' ', '')) #* WelcometoPython101:SplitandJoin

#? Exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


# new_csv = csv.split(',')
# print(new_csv) #? ['Eric', 'John', 'Michael', 'Terry', 'Graham:TerryG;Brian']

# print(','.join(csv.split(';'))) #? Eric,John,Michael,Terry,Graham:TerryG,Brian
# print(','.join(csv.split(';')).split(':')) #? ['Eric,John,Michael,Terry,Graham', 'TerryG,Brian']
# print(','.join(','.join(csv.split(';')).split(':'))) #? Eric,John,Michael,Terry,Graham,TerryG,Brian

print((','.join(','.join(csv.split(';')).split(':'))).split(',')) #? ['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']

friends_list = []
print(friends_list)

print('replace', csv.replace(';',',').replace(':',',').split(','))
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

