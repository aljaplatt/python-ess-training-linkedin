import turtle as t
import random

tim = t.Turtle()

# num_sides = 5

# #* 1 
# angle = 360 / num_sides
# tim.forward(100)
# tim.right(angle)

# #* 2 
# for _ in range(num_sides):
#     angle = 360 / num_sides
#     tim.forward(100)
#     tim.right(angle)

#* 3 

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepBlueSky", "wheat", "SeaGreen"]

def draw_shape(num_sides):
    #? set angle 
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


#? loop will call function each time increasing the number of sides
for shape_side_n in range(3, 21):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)



screen = t.Screen()
screen.exitonclick()