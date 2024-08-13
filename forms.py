from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, validators, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[ Length(max=100)])
 
    username = StringField('Username', validators=[InputRequired(message='Username is required'), Length(max=20, min=5)])
   
    password = PasswordField('Password', validators=[
        InputRequired(message='Password is required'),
        validators.EqualTo('confirm', message='Passwords don\'t match'), 
        Length(max=50, min=8, message='Password must be at least 8 characters')])
    
    
    confirm = PasswordField('confirm', validators=[
        InputRequired()])
    
    firstName = StringField('First name')
    
    lastName = StringField('Last name')
    
    submit = SubmitField('Join us', render_kw={'class':'submit'})


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message='Please enter an email address'), Length(max=100)])
    password = PasswordField('Password', validators=[InputRequired(message='Please enter a passwowrd'),  Length(max=50, min=8, message='Password must be at least 8 characters')])
    submit = SubmitField('Login', render_kw={'class':'submit'})


class Logout(FlaskForm):
    logout = SubmitField('Logout', render_kw={'class':'submit'})
