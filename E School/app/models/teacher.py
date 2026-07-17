from datetime import datetime
from app.extensions import db


class Teacher(db.Model):
    __tablename__ = "teachers"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(db.Integer, primary_key=True)

    # ---------------------------------
    # Foreign Keys
    # ---------------------------------

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False,unique=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=True)
    # ---------------------------------
    # Personal Information
    # ---------------------------------
    employee_number = db.Column(db.String(20),unique=True,nullable=False)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False
    )

    gender = db.Column(db.String(20),nullable=False)
    date_of_birth = db.Column(db.Date,nullable=True)
    phone = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(255),nullable=True)
    qualification = db.Column(db.String(150),nullable=True)
    experience = db.Column(db.Integer,nullable=True)
    joining_date = db.Column(db.Date,nullable=True)
    salary = db.Column(db.Numeric(10, 2),nullable=True)
    profile_image = db.Column(db.String(255),nullable=True)

    # ---------------------------------
    # Status
    # ---------------------------------

    is_active = db.Column(db.Boolean,default=True)
    # ---------------------------------
    # Timestamps
    # ---------------------------------
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Teacher {self.first_name} {self.last_name}>"