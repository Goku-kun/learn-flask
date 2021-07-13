from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/pages/<int:id>/values/<int:value>')
def pages_route(id, value):
    return render_template("pages.html", id=id, value=value, array=[1, 2, 3, 4])


@app.route('/extended')
def extended_page():
    return render_template("extenderpage.html")
