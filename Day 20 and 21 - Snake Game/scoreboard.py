from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        xcor = 0
        ycor = 250
        self.goto(xcor, ycor)

        self.score = 0

        with open("./Day 20 and 21 - Snake Game/data.txt") as data:
            self.highscore = int(data.read())

        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./Day 20 and 21 - Snake Game/data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1