from turtle import Turtle, Screen

t = Turtle()

for i in range(3, 11):

    cont = 1

    while cont <= i:
        t.forward(50)
        t.right(360 / i)
        cont += 1


screen = Screen()
screen.exitonclick()