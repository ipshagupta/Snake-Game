import time
from turtle import Screen
from snake import Snake, Turtle
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('Snake Game')
# switching off the screen tracer so segments can't be traced separately
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
message = Turtle()
message.hideturtle()
message.color('white')

# moving the snake in directions
screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)

# moving the snake as one
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.track_score()
        snake.grow()

    if snake.check_wall() == 1:
        is_game_on = False
        message.write("GAME OVER!", align="center", font=('Courier', 20, 'normal'))

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            message.write("GAME OVER!", align="center", font=('Courier', 20, 'normal'))

# the screen should exit only on click
screen.exitonclick()
