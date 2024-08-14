from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20,"normal"))
    
    def score_update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20,"normal"))
    
    def game_over(self):
        self.goto(0,-298)
        self.write(f"GAME OVER", align="center", font=("Arial", 25,"normal"))
        

