import colorgram
from random import choice
import turtle as t

rgb_colors = []

colors = colorgram.extract('painting.jpg',10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
turtle.penup()

turtle.setheading(180)
turtle.forward(300)
turtle.setheading(0)
turtle.speed("fastest")



for i in range(1,101):
    turtle.dot(20, choice(rgb_colors))
    turtle.forward(50)
    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
turtle.hideturtle()

screen.exitonclick()
