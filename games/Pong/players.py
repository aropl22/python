from turtle import Turtle, Screen

PADDLE_COLOR = "green"
PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5
#position = 340

class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.color(PADDLE_COLOR)
        self.penup()
        self.speed(10)
        self.goto(position,0)

    def move_up(self):
        y = self.ycor() +50
        self.goto(self.xcor(), y)
    
    def move_down(self):
        y = self.ycor() -50
        self.goto(self.xcor(), y)






