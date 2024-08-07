from turtle import Turtle
from random import randint

class Prey(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.5)
        self.color("red")
        self.penup()
        self.placement()

    def placement(self):
        x = randint(-280,280)
        y = randint(-280,280)
        self.goto(x=x, y=y)
