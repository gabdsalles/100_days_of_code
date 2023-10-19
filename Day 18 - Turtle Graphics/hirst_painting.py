import turtle
import random

turtle.colormode(255)

#import colorgram
#import os


#colors = colorgram.extract(f'{os.getcwd()}/Day 18 - Turtle Graphics/image.jpg', 30)

#rgb_colors = []

#for color in colors:

    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #rgb_colors.append((r, g, b))

#print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)

for i in range(1,65):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if i % 8 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(400)
        t.setheading(0)

screen = turtle.Screen()

screen.exitonclick()