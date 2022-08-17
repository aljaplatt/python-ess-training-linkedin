# # import another_module
# # print(another_module.another_variable)
# # from turtle import Turtle

# import turtle 

# timmy = turtle.Turtle()
# # timmy = Turtle()
# print(timmy)

# timmy.shape('turtle')
# timmy.color('coral')
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable() #* table object from the PrettyTable class ? 
print(table)

#* add column method 
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
print(table)

#* align attribute 
print(table.align ) #* {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
table.align = 'l'

print(table)
