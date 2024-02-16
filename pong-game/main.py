from turtle import Screen, Turtle, resizemode
from Score import Score
from Player import Player
WIDTH = 1200
HEIGTH = 800

# config
screen = Screen()
resizemode("noresize")
screen.title("Pong")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGTH)
screen.tracer(0)
###########################

separator = Turtle()
separator.color("white")
separator.penup()
separator.goto(0, HEIGTH // 2)
separator.setheading(270)
separator.speed("fastest")
separator.pensize(width=3)

for _ in range(HEIGTH):
  separator.pendown()
  separator.forward(15)
  separator.penup()
  separator.forward(15) 

score_x = 150
score_y = (HEIGTH //2) - 40

score_player_1 = Score((-score_x, score_y))
score_player_2 = Score((score_x, score_y))

player_x = (WIDTH // 2) - 20
player_y = 0 

player1 = Player((-player_x, player_y))

screen.listen()
screen.onkey(player1.goup, "Up")
screen.onkey(player1.godown, "Down")

is_game_on = True
while is_game_on:
  screen.update()
  
screen.mainloop()