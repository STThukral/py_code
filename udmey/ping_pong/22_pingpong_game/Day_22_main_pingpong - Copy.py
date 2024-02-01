#create the screen
#create and move the paddle
#create another paddle
#create the ball and make it move
#hitting the ball and bouncing back
#detect collision with paddle
#Detect when misses
#keep score

from turtle import Turtle,Screen
from Day_22_paddle import paddle
from Day_22_ball import ball
from Day_22_scoreboard import Scoreboard
import time

#screen object
screen = Screen()
right_paddle = paddle((350,0))
left_paddle = paddle((-350,0))
ball = ball()
scoreboard = Scoreboard()


#setup screen
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # to put the animation off so that we can't see paddle moving
#from centre to right
#but this make the paddle disappear
#so we need to write screen.update()


    
screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")

screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(.1) # to make the ball move slow , otherwise it goes really fast
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    #detect collision with x or y coordinate
    if ball.xcor() > 380:
        scoreboard.l_increment_score()
        ball.reset_position()
         
    if ball.xcor() < -380:
        scoreboard.r_increment_score()
        ball.reset_position()

    if scoreboard.l_score == 2 or scoreboard.r_score == 2:
        scoreboard.game_over()
        game_is_on =False

        

screen.exitonclick()
