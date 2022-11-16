import time

import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

wn = t.Screen()

wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("My Snake Game")
wn.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

wn.listen()
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    wn.update()
    time.sleep(0.5)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        print("Food is eaten up...")
        food.refresh()

wn.exitonclick()