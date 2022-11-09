from flask import jsonify
from . import api
from app.models import Post


@api.route('/')
def index():
    return 'Hello this is the API'


@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])

@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())
