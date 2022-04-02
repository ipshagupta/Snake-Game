from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.color('white')
        self.speed('fastest')
        rand_x = random.randint(-230, 230)
        rand_y = random.randint(-240, 220)
        self.goto(x=rand_x, y=rand_y)
        self.generate_food()

    def generate_food(self):
        rand_x = random.randint(-230, 230)
        rand_y = random.randint(-240, 220)
        self.goto(x=rand_x, y=rand_y)
