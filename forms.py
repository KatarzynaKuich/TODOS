from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField

class TodoForm(FlaskForm):
    id =StringField()
    title   = StringField()
    description    = TextAreaField()
    done = BooleanField()

