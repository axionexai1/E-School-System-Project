from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):

    email = StringField("Email Address",validators=[DataRequired(message="Email is required."),Email(message="Enter a valid email address."),Length(max=120)])
    password = PasswordField( "Password",validators=[DataRequired(message="Password is required."),Length(min=6, max=128)] )
    submit = SubmitField("Login")