#Tkinter to create GUI
#TK documentation will help you with vearious methods and functions
from tkinter import *

#creating a function to see what happens when button gets clicked
def button_clicked():
    print("I got clicked")
    input_field=input.get()   # to get the value from input filed
    my_label.config(text=input_field)


window=Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)  # padding on windows

#create lable in window
my_label = Label(text="I am a label",font=("Arial",18,"bold"))
my_label["text"] ="New Text" # This will over write the label "I am a label"
#to print the label use packer (to layout the component we are building
#my_label.pack(side ="top") # to display label in bottom

# both methods will overwrte inital methods
my_label["text"] ="New Text" # This will over write the label "I am a label"
my_label.config(text="New Text") # This will over write the label "I am a label"
my_label.grid(column =0,row=0)

window.config(padx=50,pady=50)  # padding on label
    
#Button
button = Button(text="Click Me",command=button_clicked)
#button.pack(side="top")  # to pack it on screen
button.grid(column=1,row=1)

new_button = Button(text="New BUtton",command=button_clicked)
#button.pack(side="top")  # to pack it on screen
new_button.grid(column=3,row=0)


# to get input field
input = Entry(width=10)
#input.pack()
input.grid(column =3,row=2)    
# this keeps the tkinter window open
window.mainloop()

# pack
# will pack  all widgtes in below the above one
#can help to change the position of widgets
#Place
#my_label.place(x=100,y=0) # to place any widgets in screen need to
#write it next the text declared
#Grid # easiset way to put text or button or any widgets inposition
#my_label.grid(column =0,row=0)  #position where we want to put text
#button.grid(column=1,row=1)
#NOTE :- IMPORTANT pack and grid doesnt work together will give error
#       if we try to use both code
