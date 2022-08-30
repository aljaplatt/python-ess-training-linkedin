# msg='Welcome to Python 101: Strings'
# print(msg.find('h')) #? 14 
# print(msg.find('Python')) #? 11

msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))
msg=msg.replace('Python','C')
print(msg)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
print(msg)

msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)
