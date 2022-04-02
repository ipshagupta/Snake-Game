from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 11, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(x=0, y=230)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
