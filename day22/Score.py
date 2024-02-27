from turtle import Turtle
from const import ALIGN,FONT


class Score(Turtle):
    def __init__(self, coords: tuple[float, float]) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(coords)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN,font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGN,font=FONT)

    def add_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
