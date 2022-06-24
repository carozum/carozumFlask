from flask import Flask
app = Flask(__name__)

# url / is the home page.
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/contact')
def contact():
    content = '<h1>Contact Us</h1><p>please fill the following contact form</p>'
    return content


if __name__ == "__main__":
    app.run()