from turtle import Turtle
from random import choice, randint
from config import COLORS, HEIGHT, WIDTH

class CarManager:
    def __init__(self) -> None:
        self.cars: list[Turtle] = []
        self.move_speed = 5

    def create_car(self):
        create_car = randint(1, 6)
        if create_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.goto(self.gen_randrom_pos())
            self.cars.append(new_car)

    def gen_randrom_pos(self) -> tuple[int, int]:
        y = randint( -(HEIGHT // 2 - 80), (HEIGHT // 2 - 80))
        x = WIDTH // 2
        return (x,y)

    def new_level(self):
        self.move_speed += 5

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)
