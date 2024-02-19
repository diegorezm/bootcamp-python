from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self, coords: tuple[int, int] = (0,250), hscore: int = 0) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(coords)
        self.hscore = hscore
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} , highest score: {self.hscore}", align=ALIGN,font=FONT)

    def update_score(self, new_score:int):
        self.score = new_score
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGN,font=FONT)

    def add_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
