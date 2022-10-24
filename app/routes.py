from flask import render_template
from app import app

# Create routes for our app
@app.route('/')
def index():
    user_info = {
        'username': 'cbale',
        'email': 'christianb@movies.com'
    }
    return render_template('index.html', user=user_info)


@app.route('/posts')
def posts():
    return 'Hi this is Posts!'
