from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data =pd.read_csv("data/french_words.csv")
#print(data)
# if simply try to change data to dictionary it will give French as key
#and frech words in value  and same way English as key as english words as values
#to_learn = data.to_dict()

# but we want frech word as key and enlish word as value for each word
# so we will use orient
to_learn = data.to_dict(orient="records")
#print(to_learn)

current_card ={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    #print(current_card["French"])
    # To print words on card
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer =window.after(3000,func=flip_card) # 3000 milliseconds
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

#def is_unknown():
#    to_learn.remove(current_card)
#    data=pd.DataFrame(to_learn)
#    data.to_csv("data/words_to_learn.csv") 
#    next_card()

window = Tk()
window.title("Flashy")
#window.minsize(width=700,height=500)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card) # 3000 milliseconds

canvas = Canvas(width=800,height=526,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"italic"))


 
    

#Button
cross_logo = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_logo,command=next_card)
cross_button.grid(column=0,row=1)


tick_logo = PhotoImage(file="C:/sharad/panda_scripts/udemy/31_Flash_card_project/flash-card-project-start/images/right.png")
tick_button = Button(image=tick_logo,command=next_card)
tick_button.grid(column=1,row=1)

# caaled next_card becuase when first time we arunning it
#we should not see "Title" and "word" on card we will see French and french word
next_card()


# this keeps the tkinter window open
window.mainloop()
