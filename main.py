import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

# define the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

board = Scoreboard()
snake = Snake()
food = Food()

# define the arrow/W,A,S,D keys as the movement of the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        board.reset()
        snake.reset()

    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()























screen.exitonclick()