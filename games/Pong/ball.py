from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("blue")
        self.penup()
        self.goto(0,0)
        self.speed(1)
        self.y_move = 10
        self.x_move = 10
        self.more_speed = 0.1
        
    def move(self):
        new_y = self.ycor()+self.y_move
        new_x = self.xcor()+self.x_move
        self.goto(new_x, new_y)

    def bounce (self):
        print(f"wall bounce back at: {self.ycor()}")
        self.y_move *= -1
       
    def paddle_hit(self):
        print(f"paddle bounce back at: {self.xcor()}")
        self.x_move *= -1
        self.more_speed = self.more_speed*0.9
    
    def start(self):
        self.goto(0,0)
        self.more_speed = 0.1
        self.x_move *= -1