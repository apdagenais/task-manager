from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email, Length, DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Register')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Register')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Description')
    category = SelectField(
        'Category',
        choices=[('Work', 'Work'), ('School', 'School'), ('Personal', 'Personal'), ('Other', 'Other')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Add Task')

