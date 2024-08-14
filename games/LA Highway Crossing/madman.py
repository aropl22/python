from turtle import Turtle

TURTLE_COLOR = "red"

class Madman(Turtle):
    def __init__(self, screen_width, screen_height) -> None:
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color(TURTLE_COLOR)
        self.penup()
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def start(self):
        """define starting position, requires screen height parameter"""
        self.goto(0,y=-self.screen_height/2+18)
        self.setheading(90)

    def move_up(self):
        """move car 20 to the left"""
        self.sety(self.ycor()+20)
        self.screen.update()

    def do_nothing(self):
        """blocks 'move' key"""
        self.goto(self.pos())