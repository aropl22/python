from turtle import Turtle, Screen
import time
from random import randint
from snake import Snake
from prey import Prey
from score import Score

WIDTH = 600
HEIGHT = 600
BACKGROUND = "black"

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
prey = Prey()
score = Score()

screen.update()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

continue_game = True


while continue_game:
    snake.move_forward()

    if snake.hit_wall():
        continue_game = False
        score.game_over()

    if snake.head.distance(prey) < 15:
        snake.add_bone()
        prey.placement()
        score.score_up()
    
    if snake.body_collision():
        continue_game = False
        score.game_over()

    screen.update()

screen.exitonclick()
