from turtle import Turtle, Screen
from players import Paddle
from ball import Ball
from score import Score
import time


WIDTH = 800
HEIGHT = 600
# WIDTH = 1000
# HEIGHT = 800
BGCOLOR = "black"
PADDLE1_PICES_POSITION = [(450, 40), (450, 20), (450, 0), (450, -20), (450, - 40)]
PADDLE2_PICES_POSITION = [(-450, 40), (-450, 20), (-450, 0), (-450, -20), (-450, - 40)]
PADDLE_X_POS = 360

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BGCOLOR)
screen.title("PONG GAME")
screen.tracer(0)

paddle1 = Paddle(PADDLE_X_POS)
paddle2 = Paddle(-PADDLE_X_POS)
ball = Ball()
score = Score()

screen.update()

screen.listen()

screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")

screen.update()

game_on = True
while game_on:
    
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > (HEIGHT/2)-30 or ball.ycor() < -(HEIGHT/2)+30:
        ball.bounce()
    elif ball.xcor() > 370:
        score.live_score2 += 1
        score.score_update()
        #game_on = False
        ball.start()
    elif ball.xcor() < -370:
        score.live_score1 += 1
        score.score_update()
        #game_on = False
        ball.start()
    elif (ball.xcor() > 330 and ball.distance(paddle1) < 56) or (ball.xcor() < -330 and ball.distance(paddle2) < 56):
        ball.paddle_hit()
    
    screen.update()

screen.exitonclick()