from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=random.randint(1,4), stretch_wid=1.3)
        self.penup()
        self.goto(SCREEN_WIDTH/2-40, SCREEN_HEIGHT/2-30)
        self.free = True

    def car_placement(self,screen_width, car_ypos):
        """create a car object and places it on the screen"""
        ran_color = (
            round(random.randint(100,255)),
            round(random.randint(100,255)),
            round(random.randint(100,255))
        )
        self.color(ran_color)
        self.goto(screen_width/2-40, car_ypos)
        self.free = False

    def car_move(self):
        """randomly moves car object to the left"""
        self.goto(self.xcor()-random.randint(10,50),self.ycor())