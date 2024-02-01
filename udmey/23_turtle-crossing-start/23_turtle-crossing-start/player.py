from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

ALIGNMENT="center"
FONT = ("Courier",12,"normal") 


class Player(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.goto(position)
    
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(0,-270)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align=ALIGNMENT,font=FONT)
        
