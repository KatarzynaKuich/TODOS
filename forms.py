from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FormField
from wtforms.validators import DataRequired, Email


#todos = [ {'title': 'Zakupy','description': 'Mleko, jajka, mąka, olej, papier toaletowy (jak będzie)',
#        'done': False  },{'title': 'Zrobić zadania z Pythona','description': 'Przygotować projekt z modułu i wysłać Mentorowi',
 #       'done': False    }

class TodoForm(FlaskForm):
    title   = StringField()
    description    = StringField()
    done = FormField(FlaskForm)

