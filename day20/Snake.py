from turtle import Turtle

class Snake:
    snake_body: list[Turtle]
    def __init__(self) -> None:
        self.snake_body = []
        self.default()
        self.head = self.snake_body[0]

    def default(self):
        x = 0
        y = 0
        for _ in range(0, 3):
            self.create_bodypart((x, y))
            x -= 20

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[i - 1].xcor()
            y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x_cor, y_cor)
        self.snake_body[0].forward(20)

    def create_bodypart(self, position: tuple[float, float]):
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.snake_body.append(body_part)

    def extend(self):
        self.create_bodypart(self.snake_body[-1].position())

    def left(self):
        self.snake_body[0].setheading(180)

    def right(self):
        self.snake_body[0].setheading(0)

    def up(self):
        self.snake_body[0].setheading(90)

    def down(self):
        self.snake_body[0].setheading(270)
