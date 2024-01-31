import turtle as tt

tim= tt.Turtle()
screen = tt.Screen()

#def move_forward():
#    tim.forward(10)


#screen.listen()
#screen.onkey(key="space",fun=move_forward) #move_forward is fn in fn onkey
#screen.exitonclick()


# Higher order function means it taken a function as argument in another function

tim.shape("turtle")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.right(90)

def move_clockwise():
    tim.left(90)

def clear_drawing():
    tim.clear()  ## clear the screen
    tim.penup()
    tim.home() ## bring cursor back to original position
    tim.pendown()
    
screen.listen() ## listning key board strokes
screen.onkey(key="w",fun=move_forward) #move_forward is fn in fn onkey
screen.onkey(key="s",fun=move_backward) #move_backward is fn in fn onkey
screen.onkey(key="a",fun=move_counter_clockwise) #move_counter_clockwise is fn in fn onkey
screen.onkey(key="d",fun=move_clockwise) #move_clockwise is fn in fn onkey
screen.onkey(key="c",fun=clear_drawing) #clear_drawing is fn in fn onkey


screen.exitonclick()
