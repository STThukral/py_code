from  turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400) # width and height of screen
user_bet=screen.textinput(title="Make your bet",prompt="who will win the race ? Enter a colour:")
print(user_bet)


tim1= Turtle()
tim1.shape("turtle")
tim1.color("green")
tim1.penup()
tim1.goto(x=-238,y=-150)

tim2= Turtle()
tim2.shape("turtle")
tim2.color("blue")
tim2.penup()
tim2.goto(x=-238,y=-100)

tim3= Turtle()
tim3.shape("turtle")
tim3.color("red")
tim3.penup()
tim3.goto(x=-238,y=-70)

tim4= Turtle()
tim4.shape("turtle")
tim4.color("yellow")
tim4.penup()
tim4.goto(x=-238,y=-30)


turtle_list=[]
turtle_list.append(tim1)
turtle_list.append(tim2)
turtle_list.append(tim3)
turtle_list.append(tim4)

race_is_on= True

while race_is_on:
    for turtle in turtle_list:
        print(turtle)
        rand_distance =random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_is_on =False
            winning_turtle=turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You WON the game.Winning turtle is :{winning_turtle}")
            else:
                print(f"You LOST the Game.Winning turtle is :{winning_turtle}")

screen.exitonclick()
