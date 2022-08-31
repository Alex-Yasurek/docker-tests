from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/hello/')
def hello():
    return "Hello from Home Page"

# if you access the URL without the trailing slash,
# then Flask redirects you to the URL with the trailing slash.
@home_bp.route('/home/')
def home():
    return "Home page"

# return a json object
@home_bp.route('/person/')
def hello2():
    return jsonify({'name': 'alex', 'address': 'oceanside'})
