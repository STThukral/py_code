from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() # avoids drwing up screen when move to different axis
        self.shapesize(stretch_len =0.5, stretch_wid = 0.5)
        self.color("white")
        #self.speed("40")
        #self.refresh()
        self.x_move =10
        self.y_move =10

    def move(self):
        # 10 move the ball really fast even we make it 1 its still fast
        #so used imported time in main to make it sleep in loop so that
        #we can slow it down
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move   
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *=-1
        
    def bounce_x(self):
        self.x_move *=-1   
        
            
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
