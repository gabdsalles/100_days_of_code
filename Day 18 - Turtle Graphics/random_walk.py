import turtle as t
import random

tim = t.Turtle()
tim.pensize(5)
tim.speed("fast")
t.colormode(255)

direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

for i in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(50)


screen = t.Screen()
screen.exitonclick()