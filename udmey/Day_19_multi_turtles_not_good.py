from  turtle import Turtle,Screen
import random

#tim1= tt.Turtle()
#tim2= tt.Turtle()
#tim3= tt.Turtle()
#tim4= tt.Turtle()

is_race_on = False
screen = Screen()

screen.setup(width=500,height=400) # width and height of screen
user_bet=screen.textinput(title="Make your bet",prompt="who will win the race ? Enter a colour:")
#print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20 , 50 , 80]
all_turtles = []
#tim1.shape("turtle")
#tim1.color("green")
#tim1.penup()
#tim1.goto(x=-238,y=-150)

#tim2.shape("turtle")
#tim2.color("blue")
#tim2.penup()
#tim2.goto(x=-238,y=-110)

#tim3.shape("turtle")
#tim3.color("yellow")
#tim3.penup()
#tim3.goto(x=-238,y=-70)

#tim4.shape("turtle")
#tim4.color("red")
#tim4.penup()
#tim4.goto(x=-238,y=-30)

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} is winner")
            else:
                print(f"you have lost! The {winning_color} is winner")
                
        rand_distance = random.randint(0,2)
        turtle.forward(rand_distance)

screen.exitonclick()
