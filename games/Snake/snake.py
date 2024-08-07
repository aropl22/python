from turtle import Turtle,Screen
import time

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
#START_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0),  (-160, 0), (-180, 0), (-200, 0), (-220, 0), (-240, 0)]

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.body = []
        self.new_snake()
        self.head = self.body[0]

        
    def new_snake(self):
        for position in START_POSITION:
            bone = Turtle("square")
            bone.color("green")
            bone.penup()
            bone.goto(position)
            self.body.append(bone)

    def move_forward(self):
        snake_length = len(self.body)-1
        for position in range(snake_length,0,-1):
            self.body[position].goto(self.body[position-1].pos())
        self.head.forward(20)
        time.sleep(0.1)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hit_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290:
            return True
        elif self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        else:
            return False        
        
    def add_bone(self):
        bone = Turtle("square")
        bone.color("green")
        bone.penup()
        self.body.append(bone)

    def body_collision(self):
        for position in self.body[1:]:
            if self.head.distance(position) < 15:
                return True
        return False

