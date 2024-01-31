import turtle as tt1


tt1.bgcolor('black')
tt1.pensize(2)
tt1.speed(50)  # so that circle can go fast

# loop is to print 7 colors below 5 times (i.e range(5))
for i in range(5):
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        tt1.color(color)
        
        tt1.circle(100)  #to draw a cricle with given radius
        tt1.left(10)     # pointing tilt it left just 10

    tt1.hideturtle()



# To exit window when we click on it
screen = tt1.Screen()
screen.exitonclick()
