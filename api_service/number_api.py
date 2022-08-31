from flask import Blueprint, jsonify

numbers_bp = Blueprint('numbers', __name__)

@numbers_bp.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number + 1)


@numbers_bp.route('/print/<int:num>')
def print_list(num):
    return jsonify(list(range(num)))
