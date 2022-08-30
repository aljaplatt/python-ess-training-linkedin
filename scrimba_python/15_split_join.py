# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print('Welcome to Python 101: Split and Join')

msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print('Welcome to Python 101: Split and Join')

print(msg.split())
#? ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
print(csv.split())
#? ['Eric,John,Michael,Terry,Graham']
print(csv.split(','))
#? ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print(', '.join(friends_list))
#? Eric, John, Michael, Terry, Graham
print(' '.join(friends_list))
#? Eric John Michael Terry Graham

print(''.join(msg.split()))
print(msg.replace(' ', ''))