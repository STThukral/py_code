# dynamic type change
# a=3 is integer but if we want to change a="Hello" it will change its type
# to string.
# python is strongly , dynimcally typed

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#WORK_MIN = 25
#SHORT_BREAK_MIN = 5
#LONG_BREAK_MIN = 20
# refined it for less minutes
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

reps = 0
timer  = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer) # to stop timer
    canvas.itemconfig(timer_text,text="00:00") # to rest to 00:00
    # Below are to bring it to inital state
    check_mark_label2 = Label(text="         ",font=("Arial",12,"bold"),fg=GREEN)
    check_mark_label2.grid(column =3,row=11)
    timer_label1 = Label(text=" Timer ",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
    timer_label1.grid(column =3,row=0)
    global reps
    reps=0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # to make it for 5 mins , without 60 it will be 5 secs
    # global as will be used through out the code
    global reps
    #count_down(1*60)
    work_sec = (WORK_MIN *60)/2      # divided by 2 make 1 min to 30 secs ( timer shows like 00:00:0 if we remove 2 it will be 00:00 back to original
    short_break_sec = (SHORT_BREAK_MIN * 60)/2 # divided by 2 make 1 min to 30 secs
    long_break_sec = (LONG_BREAK_MIN * 60)/2   # divided by 2 make 1 min to 30 secs

    reps += 1
    if reps > 8:
        reps = 1

    #i.e when reps is 2,4,6        
    if reps % 2 == 0:
        timer_label1 = Label(text="Break  ",font=(FONT_NAME,30,"bold"),fg=PINK,bg=YELLOW)
        timer_label1.grid(column =3,row=0)
        count_down(short_break_sec)
    #i.e when reps is 8
    elif  reps % 8 == 0:
        timer_label1 = Label(text="Break  ",font=(FONT_NAME,30,"bold"),fg=RED,bg=YELLOW)
        timer_label1.grid(column =3,row=0)
        count_down(long_break_sec)
    # i.e when reps is 1,3,5,7
    else:
        timer_label1 = Label(text=" Work  ",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
        timer_label1.grid(column =3,row=0)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #print(count)
    # as count is number of minutes we want work /break
    # this we will be getting from short_break_sec/long_break_sec/work_sec
    count_min= math.floor(count/60)
    if count_min < 10:
        count_min = "0"f'{count_min}'
    count_sec = count % 60
    #dynamic type chnage is used here
    # when counter initially shows 5:00 below will make it 5:00
    if count_sec  == 0:
        count_sec = "00"
        # when count of seconds less than 10 i.e 9 make it 09
    elif count_sec < 10:
        count_sec = "0"f'{count_sec}'

    # this is to print the timer on canvas     
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        # 1000 milliseconds, function, arguments for function
        # below will wait for 1 sec(i.e. 1000 miliseconds,
        # calls the count_down function with parameter 5 in start timer
        # that 5 will go as paramerter in count-1
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps ==2:
            check_mark_label2 = Label(text="✔",font=("Arial",12,"bold"),fg=GREEN)
            check_mark_label2.grid(column =3,row=11)
        elif reps ==4:
            check_mark_label2 = Label(text="✔✔",font=("Arial",12,"bold"),fg=GREEN)
            check_mark_label2.grid(column =3,row=11)
        elif reps ==6:
            check_mark_label2 = Label(text="✔✔✔",font=("Arial",12,"bold"),fg=GREEN)
            check_mark_label2.grid(column =3,row=11)
        elif reps ==8:
            check_mark_label2 = Label(text="✔✔✔✔",font=("Arial",12,"bold"),fg=GREEN)
            check_mark_label2.grid(column =3,row=11)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodora Timer")
window.minsize(width=300,height=400)
window.config(padx=20,pady=20,bg=YELLOW)  # padding on windows




#tkinter canvas widget
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,27,"bold"))
#canvas.pack() if using pack so can't use grid so commneted pack
canvas.grid(column =3,row=5)



timer_label1 = Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
timer_label1.grid(column =3,row=0)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=2,row=10)

check_mark_label2 = Label(font=("Arial",12,"bold"),fg=GREEN)
check_mark_label2.grid(column =3,row=11)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=7,row=10)

window.mainloop()
