import time
from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True
food = Food()
scoreboard = Scoreboard()

while game_is_on:
    # move snake
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()
    # detect collision with tail
    for item in snake.snakes[1:]:
        if snake.head.distance(item) < 10:
            scoreboard.reset_score()
            snake.reset_snake()









screen.exitonclick()

