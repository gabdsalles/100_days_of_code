from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        self.update_scoreboard()
        print('inicializou')

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def passed_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
