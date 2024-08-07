from turtle import Turtle

ALIGN = "center"

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.live_score = 0
        self.hideturtle()
        self.penup()
        self.goto(-20, 270)
        self.color("white")
        self.write(f"Score: {self.live_score}")


    def score_up(self):
        self.live_score += 1
        self.clear()
        self.write(f"Score: {self.live_score}")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False,align=ALIGN)

        
    
