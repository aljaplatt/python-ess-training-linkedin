
#* f strings

name = 'Bob' 
# greeting = f'Hello {name}'
# print(greeting)
print(f'Hello {name}')
name = 'Alex' 
print(f'Hello {name}')

#* template strings 

greeting = 'Hello {}'
with_name = greeting.format(name)
with_name_two = greeting.format('Rolf')
print(with_name)
print(with_name_two)

#? Allows you define a template, with_name and reuse with multiple values 

#* You can also create longer templates

longer_phrase = 'Hello, {}. Today is {}.'
formatted = longer_phrase.format('Maxine', 'Sunday')
print(formatted)