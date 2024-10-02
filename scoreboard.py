FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color = "black"
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align = "left", font = FONT)

    def increase_level(self):
        self.score += 1
        self.update()





