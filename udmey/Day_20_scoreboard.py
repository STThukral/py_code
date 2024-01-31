from turtle import Turtle

#constants
ALIGNMENT="center"
FONT = ("Courier",18,"normal") 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
        
        
    def Increment_score(self):
        self.score +=1
        self.clear()  # this clears the previous core and below will display the score
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align=ALIGNMENT,font=FONT)
