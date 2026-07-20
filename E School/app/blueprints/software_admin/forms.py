from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, PasswordField, SelectField,BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


# For Creating New School
class CreateSchoolForm(FlaskForm):

    school_name = StringField("School Name",validators=[DataRequired(),Length(max=200)])
    school_code = StringField( "School Code", validators=[ DataRequired(), Length(max=20) ] )
    email = EmailField(  "School Email", validators=[ DataRequired(), Email() ] )
    phone = StringField("Phone Number",validators=[DataRequired(),Length(max=20)])
    address = TextAreaField( "Address", validators=[ DataRequired(), Length(max=500) ] )
    city =StringField("City", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    submit = SubmitField("Create School")

#For Edit School Setting 
class EditSchoolForm(FlaskForm):

    school_name = StringField("School Name",validators=[DataRequired()])
    school_code = StringField("School Code",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    phone = StringField("Phone",validators=[DataRequired()])
    address = TextAreaField("Address",validators=[DataRequired()])
    city = StringField( "City",validators=[DataRequired()])
    country = StringField("Country",validators=[DataRequired()])
    submit = SubmitField("Update School")

#For creating school admin
class CreateSchoolAdmin(FlaskForm):
    full_name = StringField("Full Name",validators=[DataRequired(),Length(min=3, max=100)])
    email = StringField("Email", validators=[DataRequired(),Email()])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(min=10, max =15)])
    password= PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password= PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password must match.")])
    school = SelectField("School", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create School Admin ")
#For Edit School Admin
class EditSchoolAdminForm(FlaskForm):

    full_name = StringField("Full Name",validators=[DataRequired()])
    username = StringField("Username",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    phone = StringField("Phone Number",validators=[DataRequired()])
    school = SelectField( "Assigned School", coerce=int,validators=[DataRequired()])
    is_active = BooleanField("Active Account")
    submit = SubmitField("Update School Admin")