# copied code from https://flask.palletsprojects.com/en/2.3.x/quickstart/

from flask import Flask
app = Flask(__name__)

# decorator functions gives additional functionality or mofifies the functionality
@app.route("/")          # to show home page called python decorator 
def hello_world():
    return '<h1 style=text-align:center>Hello, World! Dave and Dad Flask coding</h1>' \
           '<p> <h1 style=text-align:center>This is paragraph.</h1></p>' \
           '<img src="https://media4.giphy.com/media/gpwkaqNdSYwqk/200w.webp?cid=ecf05e47noc2mk3thsuya0re7ab7s9usjwtbdrnhermuxpsx&ep=v1_gifs_search&rid=200w.webp&ct=g">'
           #'<img src="https://www.vets4pets.com/siteassets/species/cat/kitten/tiny-kitten-in-sunlight.jpg?w=585&scale=down" alt="Kitten" width="300" height="200">'
           
    #html rendering and style it into centre above return
    # \ is to give another line in return
    # First one is animated giphy images and seond is jpeg image. This all is HTML rendering


# this will be printed when we do http://127.0.0.1:5000/bye
@app.route("/bye")
def bye():
    return "Byeee"

#@app.route("/username/<name>")    we can do like this as well
#@app.route("/<name>")
#def greet(name):
#    return f"Hello there {name}!"

# use this url http://127.0.0.1:5000/username/sharad/24 to get output
# creating varible paths and converting the path to specified data type
#@app.route("/username/<name>")    we can do like this as well
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}, you are {number} years old!"

print(hello_world())
print(__name__)
# As mentioned below we were flask run command from command Prompt
# but with below command we can run hello.py from this script itself, using this
#command


# intially if you output below Debug mode is off we can ON in by using
# debug=True 
if __name__ == "__main__":    # name = main means we running from script itself
    #app.run(debug=True)                 # app.run will be same as flask run command from command prompt
    app.run()
    
#RUN it from command prompt

# set FLASK_APP=hello.py
# Copy hello.py in below directory and on command prompt go to the directory path
# and run "flask run"
#C:\Users\yashi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts>flask run
#<p>Hello, World! DAVE </p>
# * Serving Flask app 'hello.py'
# * Debug mode: off
#WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000
#Press CTRL+C to quit
#127.0.0.1 - - [02/Aug/2023 16:25:58] "GET / HTTP/1.1" 200 -


#OR no need to copy hello.py just set the path with .py file

#C:\Users\yashi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts>
#set FLASK_APP=C:\sharad\panda_scripts\udemy\Day_54_web_development\hello.py

#C:\Users\yashi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts>flask run
#<p>Hello, World! DAVE and DAD</p>
# * Serving Flask app 'C:\sharad\panda_scripts\udemy\Day_54_web_development\hello.py'
# * Debug mode: off
#WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000
#Press CTRL+C to quit

#C:\Users\yashi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts>


