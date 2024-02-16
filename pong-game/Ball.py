from turtle import Turtle
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.home()
        self.shape("circle")
        self.shapesize(0.7, 0.7, 1)
        self.y = 10
        self.x = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y *= -1
    def bounce_x(self):
        self.x *= -1
