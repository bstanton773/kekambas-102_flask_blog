# Import the Flask Class from the flask module
from flask import Flask


# Create an instance of the Flask class - central object of the whole app
app = Flask(__name__)


# Create routes for our app
@app.route('/')
def index():
    return 'Hello this is the index'


@app.route('/posts')
def posts():
    return 'Hi this is Posts'
