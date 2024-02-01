#Created it by myself after going through Day 55 lessons, nearly same as Angela's code

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def guess_number_msg():
    return '<h1> Guess a Number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_number=random.randint(0,9)
print(f' Random number Generated : {random_number}')

# if h1 and img tag is in single quote (i.e. ') then https should be in double quote (i.e. ").. vice-versa
@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return '<h1 style="color:red;"> Number too low ,Try Again </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        return '<h1 style="color:Blue;" > Number too High , Try Again </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else: # i.e number == random_number:
        return '<h1 style="color:Green;"> YOUUUU FOUND ME :) !! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


# This is to run the app router and any function under and decorator
# and will generate the url "Running on http://127.0.0.1:5000"
if __name__ == "__main__":    # name = main means we running from script itself
    #app.run(debug=True)                 # app.run will be same as flask run command from command prompt
    app.run()

    
                 
