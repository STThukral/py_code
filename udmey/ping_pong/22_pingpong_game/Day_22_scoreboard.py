from turtle import Turtle

ALIGNMENT ="center"
FONT=("courier",18,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f" {self.l_score}",align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(f" {self.r_score}",align=ALIGNMENT,font=FONT)


    def l_increment_score(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()
        
        

    def r_increment_score(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == 2:
            self.goto(0,0)
            self.write("Left Player won Game Over!",align=ALIGNMENT,font=FONT)
        elif self.r_score == 2:
            self.goto(0,0)
            self.write("Right Player won Game Over!",align=ALIGNMENT,font=FONT)
        
