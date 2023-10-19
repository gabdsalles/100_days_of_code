from turtle import Turtle, Screen

t = Turtle()
"""timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkgoldenrod1")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(50)
timmy_the_turtle.backward(200)"""

t.setposition(0.00, 240.00)

for i in range(4):

    t.forward(100)
    t.right(90)

screen = Screen()

screen.exitonclick()
