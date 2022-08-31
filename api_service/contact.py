from flask import Blueprint, jsonify

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/hello/')
def hello():
    return "Hello from Contact Page"

@contact_bp.route('/person/')
def contact_info():
    return jsonify({'name': 'alex', 'city': 'oceanside', 'phone': '516-555-1212'})
