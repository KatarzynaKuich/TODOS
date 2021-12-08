from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField


#todos = [ {'title': 'Zakupy','description': 'Mleko, jajka, mąka, olej, papier toaletowy (jak będzie)',
#        'done': False  },{'title': 'Zrobić zadania z Pythona','description': 'Przygotować projekt z modułu i wysłać Mentorowi',
 #       'done': False    }

class TodoForm(FlaskForm):
    title   = StringField()
    description    = TextAreaField()
    done = BooleanField()

