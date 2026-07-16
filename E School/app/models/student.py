from datetime import datetime
from app.extensions import db


class Student(db.Model):
    __tablename__ = "students"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(db.Integer, primary_key=True)

    # ---------------------------------
    #relationship

    parents=db.relationship("ParentStudent",backref="student",lazy=True, cascade="all, delete-orphan")

    # Foreign Keys
    # ---------------------------------

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False,unique=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)

    # ---------------------------------
    # Student Information
    # ---------------------------------

    admission_number = db.Column(db.String(30),unique=True,nullable=False)

    roll_number = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    date_of_birth = db.Column(db.Date,nullable=False)
    admission_date = db.Column(db.Date,nullable=False)
    phone = db.Column(db.String(20),nullable=True)
    address = db.Column(db.String(255),nullable=True)
    profile_image = db.Column(db.String(255),nullable=True)
    blood_group = db.Column(db.String(10),nullable=True)

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
        return f"<Student {self.first_name} {self.last_name}>"