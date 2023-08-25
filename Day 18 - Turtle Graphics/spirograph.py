import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

radius = 50

current_heading = tim.heading()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

while current_heading <= 360:

    tim.circle(50)
    tim.color(random_color())
    current_heading += 10
    tim.setheading(current_heading)


screen = t.Screen()
screen.exitonclick()