from turtle import Screen, Turtle
from load_data import base

screen = Screen()
screen.setup(800, 600)
screen.title("Guessing")
screen.bgcolor("black")
screen.bgpic("./blank_states_img.gif")
screen.tracer(0)

is_game_on = True
while is_game_on:
    asw = screen.textinput(title="Enter you state", prompt="Enter a state (type exit to end the game): ")

    if asw is None:
        print("Answer needed.")
        exit(1)

    asw = asw.capitalize()

    if asw == "Exit":
        exit(0)

    while asw not in base:
        asw = screen.textinput(title="Enter you state", prompt="Enter a valid state (type exit to end the game): ")

    state = base[asw]
    new_state = Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.goto(state)
    new_state.write(asw)







screen.mainloop()
