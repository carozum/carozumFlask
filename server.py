from flask import Flask, render_template
import random
from datetime import date

# app is an object, declared with the flask class, __name__ is one of its attributes. 
app = Flask(__name__)

#*******************************************************
# decorators
#*******************************************************

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_italic(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

#*******************************************************
# page home
#*******************************************************
    
# url '/' is the home page. route() is a decorator function, a method which lives inside the app object and which adds a functionality to the function that is passed inside it. @ is used to simplify the code (shortcut) 
@app.route('/')
@make_bold
@make_italic
@make_underline
def home():
    return 'Hello, World!'

#*******************************************************
# page contact
#*******************************************************

@app.route('/contact')
def contact():
    content = '''
    <h1>Contact Us</h1>
    <p>please fill the following contact form</p>
    <iframe src="https://giphy.com/embed/kyLYXonQYYfwYDIeZl" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    '''
    return content

#*******************************************************
# page user name
#*******************************************************

# extract parts that we want variable rules : you can add variable sections to a URL by making sections with <variavle_name>. Your function then receives the <variable_name> as a keyword argument. Optionnaly you can use a converter to specify the type of the argument like <converter: variable_name>. converted bu default to a string. <path:angela> <int: 31>
# I can search for /username/caro
# attention for each update in the path @app.route('...') I have to stop the server and rerun it so that changes will be taken into account -> there is a solution to that inconvenient : debug mode on (= automatic reloader + debug on)
@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"hello {name}. You are {age} years old"

#*******************************************************
# page random number
#*******************************************************

numbertoguess = random.randint(0, 9)

@app.route('/guessanumber/<int:number>')
def guess(number):
    # gifs are coming from giphy.com
    answer = f'''<div style="text-align: center">
            <iframe src="https://giphy.com/embed/xUn3CftPBajoflzROU" width="100" height="100" frameBorder="0" class="giphy-embed" allowFullScreen ></iframe>
            <h1>Guess a number between 0 and 9</h1>
            <p>You entered {number}</p>
            <p>Number to guess is {numbertoguess}</p>
            <div>'''
    if number < numbertoguess:
        answer += '<p style="color: pink; font-size: 3rem">The number entered is too low</p>' 
    elif number > numbertoguess:
        answer += '<p style="color: blue; font-size: 3rem">The number entered is too high</p>'
    else:
        answer += '''<p style="color: green; font-size: 3rem">You found me !</p><iframe src="https://giphy.com/embed/3ohzdIuqJoo8QdKlnW" width="480" height="222" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'''
    return answer


#*******************************************************
# page portfolio: rendering an HTML template 
#*******************************************************

# flask quickstart documentation : flask is a framework, not a library, so you have to follow the requirements
# 1. put your html file into a folder called "templates"
# 2. import render_template from the flask module
# 3. call the render_template() method and pass in the file name that we have : carozum.html which lives inside our templates folder
# 4. create a new directory called static to put all your images and change the path adding /static/mountain.png
# 5. you put the styles.css inside static folder
# !!! cache on chrome is a problem : hard reload shift + reload !!!
@app.route('/portfolio-carozum')
def my_portfolio():
    return render_template('carozum.html')


#*******************************************************
# html5Up.net to create a web-base name card
#*******************************************************

@app.route('/carozum-card')
def name_card():
    return render_template('carozum-card.html')


#*******************************************************
# Math problems resolution - templating language jinja
#*******************************************************

@app.route('/carozum-math')
def carozum_math():
    random_number = random.randint(1, 10)
    the_year = date.today().year
    return render_template('carozum-math.html', 
                           num = random_number,
                           current_year = the_year)



#*******************************************************
# guess gender and age of a first name - genderize.io API and Agify.io API
#*******************************************************

# 1. pip install requests
# 2. pip freeze | grep requests

import requests
import json

@app.route('/guess-name/<some_name>')
def guess_name(some_name):
    # 1. create the API URL
    gender_url = f'https://api.genderize.io?name={some_name}'
    # 2. request to get the data from the URL
    gender_response = requests.get(gender_url)
    # 3. we can get hold of the gender data in json format
    gender_data = gender_response.json()
    # 4. from the data extract the information under the key "gender"
    gender = gender_data['gender']
    
    age_url = f'https://api.agify.io?name={some_name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    count = age_data['count']
    
    
    return render_template('guess-name.html',
                           name = some_name.capitalize(),
                           gender = gender,
                           age = age,
                           count = "{:,}".format(count))

#*******************************************************
# launch the server
#*******************************************************

# to simplify server set up and launch. 
# file server will now be run in debug Mode - flask debugger
if __name__ == "__main__":
    app.run(debug=True)