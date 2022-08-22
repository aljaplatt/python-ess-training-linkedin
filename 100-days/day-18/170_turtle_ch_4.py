import turtle as t
import random 

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

# #* 1
colours = ["CornflowerBlue", "SlateGray", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen"]
# #?  0 - east, 90 - north, 180 - west, 270 - south
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')
# for _ in range(100):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# def random_line(direction):
#     angles = [45, 90, 180]

screen = t.Screen()
screen.exitonclick()