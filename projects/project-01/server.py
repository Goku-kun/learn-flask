from flask import Flask

app = Flask(__name__)


@app.route('/')
def root_path():
    text = open("index.html", "r").read()
    return text


@app.route('/printer')
def printer():
    print(__name__)
    return '<h2>printed</h2>'


@app.route('/users/<int:id>')
def users_router(id):
    print(id)
    return f"<h2>{id} is the user id.</h2>"


'''
string	accepts any text without a slash (default)
int	    accepts positive integers
float	accepts positive floating point values
path	like string but also accepts slashes
uuid	accepts UUID strings


These are the options available for the variable types used parameters in the route.
'''
