from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    # print(request.form.to_dict())
    return render_template("index.html", name=__name__)


@app.route('/form_values', methods=["get", "post"])
def form_page():
    # print(request.form.to_dict())
    return render_template('form_page.html', req=request.form.to_dict())
