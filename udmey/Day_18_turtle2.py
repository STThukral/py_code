import turtle as t
import random
tt1= t.Turtle()


#tt1.shape("triangle")
#tt1.forward(100)
#tt1.left(150)
#tt1.forward(70)
#tt1.left(30)
#tt1.left(45)
#tt1.forward(50)

colours_list =["green","blue","orange","yellow","red","brown","pink","grey","purple"]
def draw_shape(num_sides):
    angle = 360/ num_sides
    for i in range(num_sides):
        tt1.forward(100)
        tt1.right(angle)

for shape_side in range(3,11):
    tt1.color(random.choice(colours_list))
    draw_shape(shape_side)



# To exit window when we click on it
screen = t.Screen()
screen.exitonclick()
