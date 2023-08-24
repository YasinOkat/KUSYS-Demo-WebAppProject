from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired

# Define a form class "CreateUserForm"
class CreateUserForm(FlaskForm):
    # Here you define form fields, that corresponds to an input element
    first_name = StringField('First Name', validators=[DataRequired()]) # The validators are a check, it can have validadors such as max length, or data required field
    last_name = StringField('Last Name', validators=[DataRequired()])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Create User')