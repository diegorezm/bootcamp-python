from random import randint
from turtle import Turtle, Screen

colors  = ["red", "purple" , "blue", "orange", "yellow"]
y_position = -70
screen = Screen()
width = 800
height = 600
screen.setup(width, height)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles: list[Turtle] = []
turtle_size = 20

if user_bet:
    is_race_on = True

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x= - (width// 2)  ,y=y_position)
    y_position += 30
    turtles.append(new_turtle)

while is_race_on:
   for turtle in turtles:
        if turtle.xcor() > width // 2:
            _,winner = turtle.color()
            if winner == user_bet:
                print(f"You won! the winner is {winner}!")
            else:
                print(f"You lost! the winner is {winner}!")
            is_race_on = False
        rand_distance = randint(0,10) 
        turtle.forward(rand_distance)

screen.exitonclick()
