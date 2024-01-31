import turtle as t
import random



tt1 = t.Turtle()
t.colormode(255) #to use r,g, colour defination

def random_color():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    random_color=(r,g,b)
    return random_color

#colours_list =["green","blue","orange","yellow","red","brown","pink","grey","purple"]
directions=[0,90,180,270] # for directions


for i in range(1,100):
    #tt1.color(random.choice(colours_list))
    tt1.color(random_color())
    tt1.pensize(10)  #thickness of line
    tt1.speed(50)    #speed of cursor
    #tt1.speed("fastest") # or make it predefined string value
    tt1.forward(30)
    tt1.setheading(random.choice(directions))




# To exit window when we click on it
screen = t.Screen()
screen.exitonclick()
