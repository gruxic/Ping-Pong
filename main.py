from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen= Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
score=Scoreboard()
game_is_on=True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Display 
    #Detect collision with y wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detect collision with r_paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_paddle()
    if ball.xcor()>350:
        score.increase_score_l()
        ball.restart()
    if ball.xcor()<-350:
        score.increase_score_r()
        ball.restart()
    game_is_on=score.game_over_checker()
time.sleep(5)    
screen.exitonclick()