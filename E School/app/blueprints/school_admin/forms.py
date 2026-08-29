from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField,DateField, IntegerField,DecimalField
from wtforms.validators import DataRequired, Length,Optional, NumberRange , Email


class ClassForm(FlaskForm):

    class_name = StringField( "Class Name",validators=[DataRequired(),Length(max=100)])
    class_code = StringField("Class Code", validators=[DataRequired()])
    description = TextAreaField("Description")
    is_active = BooleanField("Active")
    submit = SubmitField("Save Changes")

# For Creating Section 

class SectionForm(FlaskForm):
    class_id= SelectField("Class", coerce=int, validators=[DataRequired()])
    section_name = StringField("Section Name", validators=[DataRequired(),Length(min=1, max=100)])
    section_code =StringField("Section Code", validators=[DataRequired(), Length(max=20)])
    description = TextAreaField("Description",validators=[Optional(), Length(max=25)])
    submit = SubmitField("Save Section")

# For Creating Teacher
class TeacherForm(FlaskForm):

    # ----------------------------
    # Basic Information
    # ----------------------------
    
    first_name = StringField("First Name", validators=[DataRequired(),Length(max=100)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(max=50)])
    email = StringField("Email",validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField("Phone",validators=[DataRequired(), Length(max=20)])
    # ----------------------------
    # Personal Information
    # ----------------------------
    gender = SelectField("Gender",choices=[("", "-- Select Gender --"),("Male", "Male"),("Female", "Female"),("Other", "Other")],
    validators=[DataRequired()])

    date_of_birth = DateField("Date of Birth",format="%Y-%m-%d",validators=[Optional()])
    cnic = StringField("CNIC",validators=[Optional(), Length(max=20)])
    address = TextAreaField("Address",validators=[Optional(), Length(max=255)])
    emergency_contact = StringField("Emergency Contact",validators=[Optional(), Length(max=20)])
    blood_group = SelectField("Blood Group",choices=[("", "-- Select Blood Group --"),("A+", "A+"),("A-", "A-"),("B+", "B+"),("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-")
    ],
    validators=[Optional()])

    # ----------------------------
    # Professional Information
    # ----------------------------
    qualification = StringField("Qualification",validators=[Optional(), Length(max=150)])
    experience = IntegerField("Experience (Years)",validators=[Optional(), NumberRange(min=0)])
    joining_date = DateField("Joining Date",format="%Y-%m-%d",validators=[DataRequired()])
    salary = DecimalField("Salary",places=2,validators=[Optional(), NumberRange(min=0)])
    employment_status = SelectField("Employment Status",choices=[("Active", "Active"),("On Leave", "On Leave"),
    ("Resigned", "Resigned"),
    ("Suspended", "Suspended")
    ],
    validators=[DataRequired()]
    )
    profile_image = StringField("Profile Image",validators=[Optional(), Length(max=255)])
    notes = TextAreaField("Notes",validators=[Optional()])
    # ----------------------------
    # Relationships
    # ----------------------------
    managed_class_id = SelectField("Managed Class",coerce=int,validators=[Optional()])
    # ----------------------------
    # Buttons
    # ---------------------------
    submit = SubmitField("Save Teacher")


# Form for Teacher Subject 

class TeacherSubjectForm(FlaskForm):
    teacher_id = SelectField("Teacher",coerce=int,validators=[DataRequired()])
    class_id = SelectField("Class",coerce=int,validators=[DataRequired()])
    section_id = SelectField("Section",coerce=int,validators=[DataRequired()])
    subject_id = SelectField("Subject",coerce=int,validators=[DataRequired()])
    academic_year = StringField("Academic Year",validators=[DataRequired()])
    is_active = SelectField("Status",choices=[(1, "Active"),(0, "Inactive")],coerce=int,validators=[DataRequired()])
    submit = SubmitField("Save")


# For Creating Subject 
class SubjectForm(FlaskForm):

    subject_name = StringField("Subject Name",validators=[DataRequired(),Length(min=2, max=100)])
    subject_code = StringField("Subject Code",validators=[DataRequired(),Length(min=2, max=20)])
    description = TextAreaField("Description", validators=[Length(max=500)])
    is_active = SelectField( "Status",choices=[ (1, "Active"),(0, "Inactive")],
    coerce=int,validators=[DataRequired()])
    submit = SubmitField("Save Subject")



# -------------------------------------------
#   ------ Student Management Form ----------------
# ---------------------------------------------

class StudentForm(FlaskForm):

# -------------------------
# Personal Information
# -------------------------

    first_name = StringField("First Name",validators=[DataRequired(),Length(max=50)])
    last_name = StringField("Last Name",validators=[DataRequired(),Length(max=50)])
    email = StringField("Email",validators=[DataRequired(),Email(),Length(max=120)])
    phone = StringField("Phone",validators=[Optional(),Length(max=30)])
    gender = SelectField("Gender",choices=[("", "-- Select Gender --"),("Male", "Male"),("Female", "Female"),("Other", "Other")],validators=[DataRequired()])
    date_of_birth = DateField("Date of Birth",format="%Y-%m-%d",validators=[Optional()])
    cnic = StringField("CNIC",validators=[Optional(),Length(max=30)])
    # -------------------------
    # Academic Information
    # -------------------------
    admission_number = StringField("Admission Number",validators=[DataRequired(),Length(max=50)])
    roll_number = StringField("Roll Number",validators=[Optional(),Length(max=30)])
    class_id = SelectField("Class",coerce=int,choices=[],validators=[DataRequired()])
    section_id = SelectField("Section",coerce=int,choices=[],validators=[DataRequired()])
    admission_date = DateField("Admission Date",format="%Y-%m-%d",validators=[Optional()])
    # -------------------------
    # Parent / Guardian
    # -------------------------
    guardian_name = StringField("Guardian Name",validators=[Optional(),Length(max=100)])
    guardian_phone = StringField("Guardian Phone",validators=[Optional(),Length(max=30)])
    # -------------------------
    # Address
    # -------------------------
    address = TextAreaField("Address",validators=[Optional(),Length(max=500)])
    # -------------------------
    # Submit
    # -------------------------
    submit = SubmitField("Save Student")
