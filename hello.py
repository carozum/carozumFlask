from flask import Flask

# app is an object, declared with the flask class, __name__ is one of its attributes. 
app = Flask(__name__)

# url '/' is the home page. route() is a decorator function, a method which lives inside the app object and which adds a functionality to the function that is passed inside it. @ is used to simplify the code (shortcut) 
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/contact')
def contact():
    content = '''
    <h1>Contact Us</h1>
    <p>please fill the following contact form</p>
    <iframe src="https://giphy.com/embed/kyLYXonQYYfwYDIeZl" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    '''
    return content

# extract parts that we want variable rules : you can add variable sections to a URL by making sections with <variavle_name>. Your function then receives the <variable_name> as a keyword argument. Optionnaly you can use a converter to specify the type of the argument like <converter: variable_name>. converted bu default to a string. <path:angela> <int: 31>
# I can search for /username/caro
# attention for each update in the path @app.route('...') I have to stop the server and rerun it so that changes will be taken into account -> there is a solution to that inconvenient : debug mode on (= automatic reloader + debug on)
@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"hello {name}. You are {age} years old"

# to simplify server set up and launch. 
# file server will now be run in debug Mode - flask debugger
if __name__ == "__main__":
    app.run(debug=True)