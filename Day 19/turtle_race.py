from turtle import Turtle, Screen
import random

def initialize_turtles():

    turtles_list = []
    colors_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    y_axis = 100

    for _ in range(7):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.goto(x=-230, y=y_axis)
        y_axis -= 30
        color_chosen = random.choice(colors_list)
        turtle.color(color_chosen)
        colors_list.remove(color_chosen)
        #turtle.pendown()
        turtles_list.append(turtle)

    return turtles_list

def race(turtles_list):

    is_race_on = True
    
    while is_race_on:

        for turtle in turtles_list:
            
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                is_race_on = False
                if winning_color == user_bet:
                    print(f"Você venceu! A tartaruga {winning_color} é a vencedora.")
                else:
                    print(f"Você perdeu :/ A tartaruga {winning_color} é a vencedora. Sua aposta foi {user_bet}.")
                break

            turtle.forward(random.randint(1, 15))

        

    
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Faça sua aposta", prompt="Qual tartaruga você acha que ganhará a corrida?")
turtles_list = initialize_turtles()
race(turtles_list=turtles_list)


screen.exitonclick()