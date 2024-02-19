from turtle import Turtle
from config import HEIGHT

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto_start()

    def move_up(self):
        if self.ycor() > (HEIGHT // 2 -40):
            return
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        if self.ycor() < -(HEIGHT // 2 - 40):
            return
        self.setheading(270)
        self.forward(20)

    def goto_start(self):
        self.goto(0, -(HEIGHT // 2 - 20))

