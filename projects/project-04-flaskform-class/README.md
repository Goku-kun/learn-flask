# Forms in Flask

A Flask Form class inherits from the class `FlaskForm` and includes attribute for every field

A common practice when creating web forms with flask is to put them in their own separate file and them import them into the app file.

```python
class MyForm(FlaskForm):
  my_textfield = StringField("Text Label")
  my_submit = SubmitField("Submit label")
```

`FlaskForm` is part of [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/)

## Creating the Form

By accessing the attributes of the form passed to the template, the form can be created.

Go to the template file and we use

```handlebars
<form method="post" action="{{ url_for('form_function') }}">
  {{ template_form.hidden_tag()}}
  {{ template_form.my_textfield.label }}
  {{ template_form.my_textfield() }}
  {{ template_form.my_submit() }}
</form>
```

Back in the server.py file, the form instance can be created and shared as follows:

```py

class MyForm(FlaskForm):
  my_textfield = StringField("Text Label")
  my_submit = SubmitField("Submit label")


comments = []
@route('/')
def index():
  form_instance = MyForm()
  textfield_value = form_instance.my_textfield.data
  comments.append(textfield_value)
  return render_template('index.html', template_form=form_instance, comments = comments)
```

## Validation

Validation is when form fields must contain data or a certain format of data in order to move forward with submission.

Validators come from the `wtform.validators` module. Importing the `DataRequired()` validator is accomplished like this:

```py
from wtforms.validators import DataRequired


my_textfield = StringField("TextLabel", validators=[DataRequired()])
```

The `DataRequired()` validator simply requires a field to have something in it before the form is submitted.

The `validators` argument takes a list of validator instances.

The FlaskForm class also provides a method called `validate_on_submit()`, which we can used in our route to check for a valid form submission.

```py
if my_form.validate_on_submit():
    # get form data
else:
    # render form again because of invalid data
```

The validate_on_submit() function returns True when there is a POST request and all the associated form validators are satisfied.

## Other Form Elements

1. TextAreaField()

The TextAreaField is a text field that supports multi-line input. The data returned from a TextAreaField instance is a string that may include more whitespace characters such as newlines or tabs.

`text_area = TextAreaField("Text Area Label")`

2. BooleanField()

A checkbox element is created using the BooleanField object. The data returned from a BooleanField instance is either True or False.

`check_box = BooleanField("Check this")`

3. RadioField()

A radio button group is created using the RadioField object. Since there are multiple buttons in this group, the instance declaration takes an argument for the group label and a keyword argument choices which takes a list of tuples.

Each tuple represents a button in the group and contains the button identifier string and the button label string.

```py

my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), ("id2","Two"), ("id3","Three")])
```

Since the RadioField() instance generally contains multiple buttons it is necessary to iterate through it to access the components of the subfields.

```handlebars
{% for btn in template_form.my_radio_group %}
      <!-- Put the button variable then the button label
      in the following td tags-->
      <td>{{btn()}}</td>
      <td>{{btn.label}}</td>
    {% endfor %}


<!-- It would generate something like follows: -->
    <td><input type="radio" id="id1" name="id1" value="One" /></td>
    <td><label for="id1" >One</label></td>
    <td><input type="radio" id="id2" name="id2" value="Two" /></td>
    <td><label for="id2">Two</label></td>
    <td><input type="radio" id="id3" name="id3" value="Three" /></td>
    <td><label for="id3">Three</label></td>
```

## Redirecting after Form Submission

We can manually redirect by specifying the action property of the form.

The other way is to use the `redirect("url string")`.

Using this function inside another route will simply send us to the URL we specify. In the case of a form submission, we can use redirect() after we have processed and saved our data inside our validate_on_submit() check.
