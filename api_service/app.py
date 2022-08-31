# https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
# https://medium.com/analytics-vidhya/swagger-ui-dashboard-with-flask-restplus-api-7461b3a9a2c8
# https://medium.com/bb-tutorials-and-thoughts/how-to-dockerize-the-python-rest-api-with-flask-library-d2b51dd4a0ae
from flask import Flask

from contact import contact_bp
from home import home_bp
from number_api import numbers_bp

app = Flask(__name__)
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(numbers_bp, url_prefix='/numbers')

# if __name__ == "__main__":
#     app.run()

# @app.route('/<int:number>/')
# def incrementer(number):
#     return "Incremented number is " + str(number + 1)


# @app.route('/numbers/<int:num>')
# def print_list(num):
#     return jsonify(list(range(num)))


# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name


# # return a json object
# @app.route('/person/')
# def hello2():
#     return jsonify({'name': 'Jimit', 'address': 'India'})

# call this before every request is processed
# @app.before_request
# def before():
#     print("This is executed BEFORE each request.")


# if you access the URL without the trailing slash,
# then Flask redirects you to the URL with the trailing slash.
# @app.route('/home/')
# def home():
#     return "Home page"


# if you access the URL with the trailing slash,
# then it will result in status 404 Not Found or redirect to function hello().
# @app.route('/contact')
# def contact():
#     return "Contact page"

# this will be called form command line in docker
# if testing not in docker then uncomment and run "python3 app.py"
# app.run()
