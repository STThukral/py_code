from tkinter import *

def button_clicked():
    print("I got clicked")
    input_field=input.get()   # to get the value from input filed
    my_label.config(text=int(input_field)*1.6)


window=Tk()
window.title("Miles to Km Converter")
window.minsize(width=300,height=150)
window.config(padx=20,pady=20)  # padding on windows


# to get input field Entry widgets
input = Entry(width=10)
#input.pack()
input.grid(column =7,row=0)    

my_label1 = Label(text="Miles",font=("Arial",12,"bold"))
my_label1.grid(column =8,row=0)

my_label2 = Label(text="is Equal to",font=("Arial",12,"bold"))
my_label2.grid(column =1,row=2)


my_label = Label(text="0",font=("Arial",12,"bold"))
my_label.grid(column =7,row=2)

my_label3 = Label(text="Km",font=("Arial",12,"bold"))
my_label3.grid(column =9,row=2)

#Button
button = Button(text="Calculate",command=button_clicked)
#button.pack(side="top")  # to pack it on screen
button.grid(column=7,row=10)


# this keeps the tkinter window open
window.mainloop()
