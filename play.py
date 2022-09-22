import random

names_string = input("Give me everybody's names, separated by a comma: ")
# alex, kelly, jose, hajara
names = names_string.split(", ")
print(names) # ['alex', 'kelly', 'jose', 'hajara']
# random_name = random.choice(names)
# print(f'{random_name} is going to buy the meal today!')