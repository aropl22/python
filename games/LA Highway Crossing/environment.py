from turtle import Turtle
import random

STREET_COLOR = "white"
ran_color = ()
#

class Environment(Turtle):
    def __init__(self,screen_width,screen_height) -> None:
        super().__init__()
        self.penup()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.car_lines = []

    def draw_street(self):
        """draw street and lines, requires screen width and height"""
        
        self.pencolor(STREET_COLOR)
        self.pensize(5)
        self.hideturtle()

        # draw road

        self.goto(-self.screen_width/2, self.screen_height/2-40)
        self.pendown()
        self.goto(self.screen_width/2, self.screen_height/2-40)
        self.penup()
        self.goto(-self.screen_width/2, -self.screen_height/2+40)
        self.pendown()
        self.goto(self.screen_width/2, -self.screen_height/2+40)
        self.penup()
        

        # draw lines

        self.pensize(2)
        line_width = (self.screen_height-80)/8
        line_start_height = self.screen_height/2-40
        self.car_lines.append(line_start_height-line_width/2)

        for line in range(7):
            line_y_pos = line_start_height-line_width
            self.goto(-self.screen_width/2,line_y_pos)
            self.car_lines.append(line_y_pos - line_width/2)
            progress = -self.screen_width/2

            while progress < self.screen_width/2:
                self.penup()
                self.forward(20)
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)
                progress += 40

            line_start_height -= line_width
                  


