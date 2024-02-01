import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player((0,-270))
scoreboard = Scoreboard()
car_Manager = CarManager()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    #read the file after as game starts (high score)
    scoreboard.prev_high_score()
    time.sleep(0.1)
    screen.update()
    car_Manager.create_car()
    car_Manager.move_cars()

    # player reach finish line
    # reset player position back to inital position
    if player.ycor() > 290:
        scoreboard.increment_score()
        player.reset_position()
        car_Manager.level_up()
        #print (f' level up : {car_Manager.level_up()}')
        

    # Detect the collision
    for car in car_Manager.all_cars:
        if car.distance(player) < 20:
            #write into file final score 
            scoreboard.write_score_to_file()
            player.game_over()
            game_is_on = False
        



screen.exitonclick()
