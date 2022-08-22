import turtle as t
import random 

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


tim.speed('fastest')

# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100) # 100 = radius
#     tim.setheading(tim.heading() + 10)

def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100) # 100 = radius
        tim.setheading(tim.heading() + size_of_gap)

draw_spiro(5)


screen = t.Screen()
screen.exitonclick()