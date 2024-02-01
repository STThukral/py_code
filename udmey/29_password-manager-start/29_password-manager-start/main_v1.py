from tkinter import *
import string
import secrets
from tkinter import messagebox # need to write this line becuase above tkinter imprt * doenst import messagebox
import random

# to copy an paste to where want to use password directly to site, we need to install it
#import pyperclip
#pyperclip.copy("copy test")
#pyperclip.paste()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    
    print("Random password generation ")
   
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
           ,'n','o','p','q','r','s','t','u','v','w','x','y','z'
           ,'A','B','C','D','E','F','G','H','I','J','K','L','M'
           ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers= ['0','1','2','3','4','5','6','7','8','9']
    symbols= ['!','£','$','%','^','&','*','(',')','_','+']

    print("Welcome to the password generator!")
    nr_letters=4  # we can also use random.randint(8,10) just to get random no of letters we want in password
    nr_numbers=4
    nr_symbols=4

    random_letter_list= []
    random_num_list= []
    random_symbol_list= []
    
    #for char in range(1,nr_letters+1):
    #    random_passwd_list.append( random.choice(letters))
    
    # writing above in comprehension list , remeber brackest shoud be square for list
    random_letter_list=[random.choice(letters) for char in range(nr_letters)]
     
    #for num in range(1,nr_numbers+1):
    #    random_passwd_list.append(random.choice(numbers))
    
    random_num_list=[random.choice(numbers) for num in range(nr_numbers)]
    
    #for symb in range(1,nr_symbols+1):
    #    random_passwd_list.append(random.choice(symbols))
    random_symbol_list=[random.choice(symbols) for symb in range(nr_symbols)]

    password_list = random_letter_list + random_num_list + random_symbol_list
    
    
    random.shuffle(password_list)

    #passwd=""
    #for i in password_list:
    #    passwd += i

    #INSTEAD of doing above loop we can use join method
    password = "".join(password_list)
    print(f' Your new password is : {password}')
    passwd_input.insert(0,password)  #to insert generated password to entry text next to generate button
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwd(): 
    web_input=website_input.get()
    eml_input=email_input.get()
    pwd_input=passwd_input.get()
    if len(web_input.strip()) ==0 or len(pwd_input.strip())== 0:
        message_output =messagebox.showinfo(title="missing values",message="Please Enter all values")

    else:
        #messagebox.showinfo(title="Confirmaiton message",message="message")
        message_output =messagebox.askokcancel(title=web_input,message="Do you want to commit the changes")

        #message_output is boolean ... will be true or false    
        if message_output:
            piped_text =f'{web_input} | {eml_input} | {pwd_input}'
            print("Writing and appending Files")

            emp_file = open("password_file.txt", "a") #append file
            emp_file.write("\n") #\n is to append line in file with ne line
            emp_file.write(piped_text)
            emp_file.close()
   
            # to make the entry text empty once we pressed add button to add entries in file
            website_input.delete(0,END) 
            #email_input.delete(0,END)  we dont want email to get removed 
            passwd_input.delete(0,END) 
    # ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.minsize(width=400,height=350)
window.config(padx=20,pady=20)  # padding on windows


#tkinter canvas widget
canvas = Canvas(width=200,height=200, highlightthickness=0)
logo_png=PhotoImage(file="logo.png")
# x and y position of imag on canvas
canvas.create_image(100,100,image=logo_png)
#canvas.pack()
canvas.grid(column =1,row=0)


# label names
website_label_name = Label(text="Website",font=("Arial",8,"bold"))
website_label_name.grid(column =0,row=1)

email_label_name = Label(text="Email/Username",font=("Arial",8,"bold"))
email_label_name.grid(column =0,row=2)

passwd_label_name = Label(text="Password",font=("Arial",8,"bold"))
passwd_label_name.grid(column =0,row=3)


#Label entry widgets
# to get input field Entry widgets
website_input = Entry(width=35)
website_input.grid(column =1,row=1,columnspan=2)
website_input.focus()          # to bring the blinking cursor on website entry , when press f5

email_input = Entry(width=35)
email_input.grid(column =1,row=2,columnspan=2)
email_input.insert (0,"angela@gmail.com") # to add defualt entry at the begining
#email_input.insert (END,"angela@gmail.com") # to add defualt entry at the end

passwd_input = Entry(width=21)
passwd_input.grid(column =1,row=3)




#Button
button = Button(text="Generate Password",command=generate_passwd)
button.grid(column=2,row=3)


button = Button(text="Add",width=36,command=save_passwd)
button.grid(column=1,row=4)




# this keeps the tkinter window open
window.mainloop()
