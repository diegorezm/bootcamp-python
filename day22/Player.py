from turtle import Turtle
from const import HEIGTH 

class Player(Turtle):
  def __init__(self, coords: tuple[float, float]) -> None:
    super().__init__()
    self.color("white")
    self.penup()
    self.goto(coords)
    self.shape("square")
    self.shapesize(5,1)
  
  def goup(self):
    if self.ycor() > ((HEIGTH // 2) - 80):
      return
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def godown(self):
    if self.ycor() < -((HEIGTH // 2) - 80):
      return
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
