from turtle import Screen,colormode
from entities.Player import Player
from entities.Score import Score
from entities.Car import CarManager
from config import WIDTH, HEIGHT
from time import sleep

screen = Screen()
screen.setup(WIDTH, HEIGHT)
colormode(255)
screen.title("Pong")
screen.bgcolor("white")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

score_y = (HEIGHT // 2 - 40)
score_x = -(WIDTH // 2 - 80)
score = Score((score_x, score_y))

car_manager = CarManager()

is_game_on = True

while is_game_on:
    screen.update()
    sleep(0.1)
    car_manager.move()
    if len(car_manager.cars) < 15:
        car_manager.create_car()
    if player.ycor() > (HEIGHT // 2 - 40):
        score.add_score()
        player.goto_start()
        car_manager.new_level()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            is_game_on = False
        if car.xcor() < -(WIDTH // 2):
            car.goto(car_manager.gen_randrom_pos()) 

screen.mainloop()
