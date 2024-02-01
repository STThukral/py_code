from tkinter import *
import requests

#global Kanye_quote
def get_quote():
    response =requests.get(url="https://api.kanye.rest")
    response.raise_for_status
    print(response) # got 200, so this means request successful
    data=response.json()
    print(data)
    Kanye_quote= data["quote"]
    print(Kanye_quote)
    # this is to print the quotes in "text" in quote_text
    canvas.itemconfig(quote_text,text=Kanye_quote)
    

   



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="kanye quotes here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
