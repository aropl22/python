from turtle import Turtle


class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.live_score1 = 0
        self.live_score2 = 0
        self.hideturtle()
        self.penup()
        self.goto(-50, 220)
        self.color("white")
        self.write(f"{self.live_score2} : {self.live_score1}", font=("Arial", 40, "normal"))

    def score_update(self):
        self.clear()
        self.write(f"{self.live_score2} : {self.live_score1}", font=("Arial", 40, "normal"))
