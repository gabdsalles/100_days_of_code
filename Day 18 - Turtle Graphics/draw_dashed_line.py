from turtle import Turtle, Screen

t = Turtle()
t.pu()
t.setposition(-240.00, 0.00)
t.pd()

for i in range(50):
    t.forward(10)
    if i % 2 == 0:
        t.pu()
    else:
        t.pd()

screen = Screen()
screen.exitonclick()