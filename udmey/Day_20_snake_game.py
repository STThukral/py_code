from turtle import Screen,Turtle
from Day_20_snake import Snake
from Day_20_food import Food
from Day_20_scoreboard import Scoreboard
import time

screen =Screen()

screen.setup(width =600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food =Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score =0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # move forward and tail to follow
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.Increment_score()
        #new_segment = Turtle("square")
        snake.extend()
        food.refresh()
        #print("nom nom nom")
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #print("Game Over")
        scoreboard.game_over()
        game_is_on =False

    # this works but creating the same logic with slice
    #for segment in snake.segments:
    #    if segment == snake.head:
    #        pass
    #    elif snake.head.distance(segment) < 10:
    #        #print("Game Over")
    #        scoreboard.game_over()
    #        game_is_on =False

    # used python slicing feature to slice the segment
    # and snake.segments[1:] to exclude head segment
    # and take allother segment and see if head collides
    #with them and game stops
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #print("Game Over")
            scoreboard.game_over()
            game_is_on =False    
screen.exitonclick()








