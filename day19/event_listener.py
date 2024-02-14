from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()

def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def move_backwards():
    turtle.backward(25)

def move_fowards():
    turtle.forward(25)

def clear():
    turtle.home()
    turtle.clear()

screen.onkeypress(move_fowards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear, "c")


screen.exitonclick()
