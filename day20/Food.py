from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("orange")
        self.speed("fastest")
        self.randomize_path()

    def randomize_path(self):
        x_cor = randint(-250, 250)
        y_cor = randint(-250, 250)
        self.goto(x_cor, y_cor)
