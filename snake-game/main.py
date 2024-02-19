from turtle import Screen 
from Snake import Snake
from Food import Food
from Score import Score
import time

screen = Screen()
width = 600
heigth = 600
screen.setup(width, heigth)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()

with open("hscore.txt", 'r') as file:
    content = file.read().strip()

try:
    score = int(content)
except ValueError as e:
    raise e
scoreboard = Score((0, 250),score)


game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake_head_x = snake.head.xcor()
    snake_head_y = snake.head.ycor()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.randomize_path()
        scoreboard.add_score()

    if snake_head_x > 280 or snake_head_x < -280 or snake_head_y > 280 or snake_head_y < -280:
        scoreboard.game_over()
        if score < scoreboard.score:
            with open("hscore.txt", "w") as file:
                file.write(f"{scoreboard.score}")
        game_is_on = False
    for body_part in snake.snake_body[1:]:
        if body_part == snake.head:
            pass
        elif snake.head.distance(body_part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.mainloop()
