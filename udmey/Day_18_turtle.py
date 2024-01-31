from turtle import Turtle,Screen

timmy_the_turtle = Turtle()    # first object is timmy_the_turtle

#To make turtle make square
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)


# another easy way is to write it in loop
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)



tt = Turtle()  # create another object of turtle i.e.tt, which will be second turtle
color_list =["red","blue","yellow","green"]
tt.shape("turtle")



# Chnage 4 colors and run it 4 time to make square for every color
for n in range(len(color_list)):
    tt.color(color_list[n])
    for i in range(4):
        tt.forward(50)
        tt.left(90)    
    for i in range(4):
        tt.forward(100)
        tt.left(90)


###############
###############

tt1 = Turtle()

#draw a line with dots and spaces
def drawdot(space,x):
  for i in range(x):
    for j in range(x):
       tt1.dot()
    tt1.forward(space)
    tt1.forward(space*x)


tt1.penup()
drawdot(2,10)
tt1.shape("turtle")
tt1.color("orange")

# drwa dotted line
tt2 = Turtle()
for i in range(15):
    tt2.forward(18)
    tt2.penup()
    tt2.forward(10)
    tt2.pendown()
tt2.shape("turtle")
tt2.color("pink")
    
# To exit window when we click on it
screen = Screen()
screen.exitonclick()
