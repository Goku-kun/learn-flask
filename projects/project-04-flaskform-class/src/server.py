from flask import Flask, render_template,
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import SomeForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"


class MyForm(FlaskForm):
    my_textfield = StringField("Text Label", validators=[DataRequired()])
    my_submit = SubmitField("Submit label")


list_of_comments = []


@app.route('/', methods=["POST", "GET"])
def index_route():
    flask_form = MyForm()
    if flask_form.validate_on_submit():
        list_of_comments.append(flask_form.my_textfield.data)
    else:
        pass
    return render_template('index.html', template_form=flask_form, comments=list_of_comments)
