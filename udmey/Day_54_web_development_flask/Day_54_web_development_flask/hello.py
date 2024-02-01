# copied code from https://flask.palletsprojects.com/en/2.3.x/quickstart/

from flask import Flask
app = Flask(__name__)

# decorator functions gives additional functionality or mofifies the functionality
@app.route("/")          # to show home page called python decorator 
def hello_world():
    return "<p>Hello, World! Dave and Dad's Flask coding</p>"


# this will be printed when we do http://127.0.0.1:5000/bye
@app.route("/bye")
def bye():
    return "Byeee"
    

print(hello_world())
print(__name__)
# As mentioned below we were flask run command from command Prompt
# but with below command we can run hello.py from this script itself, using this
#command

if __name__ == "__main__":    # name = main means we running from script itself
    app.run()                 # app.run will be same as flask run command from command prompt

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


