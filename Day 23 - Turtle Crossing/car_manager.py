from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

"""Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
 and move to the left edge of the screen. No cars should be generated in the top and bottom 50px
   of the screen (think of it as a safe zone for our little turtle).
 Hint: generate a new car only every 6th time the game loop runs. 
 If you get stuck, check the video walkthrough in Step 4."""


class CarManager:
    
    def __init__(self):
        
        self.cars_list = []
        self.create_car()
        self.level = 0

    def create_car(self):

        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.penup()
        random_y = randint(-250, 250)
        car.goto(300, random_y)
        self.cars_list.append(car)

    def update_cars(self):

        for car in self.cars_list:

            car.goto(car.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * self.level , car.ycor())

