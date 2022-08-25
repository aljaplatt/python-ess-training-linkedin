###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turtle_module
import random
import sys 

print(sys.prefix)

rgb_colors = []
colors = colorgram.extract('100-days/day-18/image.jpg', 30)
# print('COLORS', colors)
for color in colors:
    # rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

#? set to rgb ?  
turtle_module.colormode(255)
tim = turtle_module.Turtle()

#? dot is part of the turtle module 
# tim.dot(20, random.choice(rgb_colors))






screen = turtle_module.Screen()
screen.exitonclick()