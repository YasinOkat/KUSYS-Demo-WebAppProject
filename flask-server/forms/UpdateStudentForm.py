from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField


class UpdateStudentForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    birth_date = DateField('Birth Date', format='%Y-%m-%d')
    username = StringField('Username')
    role = BooleanField('Admin')
    submit = SubmitField('Update User')
