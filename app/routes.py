from app import app

# Create routes for our app
@app.route('/')
def index():
    return 'Hello this is the index'


@app.route('/posts')
def posts():
    return 'Hi this is Posts'