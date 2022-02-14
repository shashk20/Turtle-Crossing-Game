FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200,250)
        self.ht()
        self.score=1
        self.print()
    def scoreup(self):
        self.clear()
        self.score+=1
        self.print()
    def print(self):
        self.write(f"Level: {self.score}", move=True, align="center", font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",48,"normal"))