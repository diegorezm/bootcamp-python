from turtle import Screen, Turtle, resizemode
from time import sleep
from Score import Score
from Player import Player
from Ball import Ball
from const import HEIGTH, WIDTH

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

score_x = int(150)
score_y = (HEIGTH //2) - 40

score_player_1 = Score((-score_x, score_y))
score_player_2 = Score((score_x, score_y))

player_x = (WIDTH // 2) - 20
player_y = 0

player1 = Player((-player_x, player_y))
player2 = Player((player_x, player_y))

screen.listen()
#p1
screen.onkey(player1.goup, "Up")
screen.onkey(player1.godown, "Down")
#p2
screen.onkey(player2.goup, "w")
screen.onkey(player2.godown, "s")

ball = Ball()

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    sleep(0.04)

    # checking collision with top wall
    if ball.ycor() > (HEIGTH // 2 - 20) or ball.ycor() < -(HEIGTH // 2 - 20):
      ball.bounce_y()

    if ball.xcor() > (WIDTH // 2 - 5) or ball.xcor() < -(WIDTH // 2 - 5):
        ball.home()
        sleep(1)
    
    if ball.distance(player2) < 40 and ball.xcor() > 420:
        ball.bounce_x()
        score_player_2.add_score()

    if ball.distance(player1) < 40 and ball.xcor() < -420:
        ball.bounce_x()
        score_player_1.add_score()

screen.mainloop()
