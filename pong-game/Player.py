from turtle import Turtle
class Player(Turtle):
  def __init__(self, coords: tuple[int]) -> None:
    super().__init__()
    self.color("white")
    self.penup()
    self.goto(coords)
    self.shape("square")
    self.shapesize(5,1)
  
  def goup(self):
    new_y = self.xcor() + 20
    self.goto(self.xcor(), new_y)

  def godown(self):
    new_y = self.xcor() - 20
    self.goto(self.xcor(), new_y)