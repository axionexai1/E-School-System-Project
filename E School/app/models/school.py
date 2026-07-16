from.section import Section
from datetime import datetime
from app.extensions import db
from app.models.subject import Subject


class School(db.Model):
    __tablename__ = "schools"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # School Information
    school_name = db.Column(db.String(150), nullable=False)
    school_code = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    website = db.Column(db.String(150), nullable=True)
    logo = db.Column(db.String(255), nullable=True)

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime,default=datetime.utcnow)

    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # --------------------------
    # Relationships
    # --------------------------

    users = db.relationship("User",backref="school",lazy=True,cascade="all, delete-orphan")
    section = db.relationship("Section",backref="school",lazy=True,cascade="all, delete-orphan")
    school_admins = db.relationship("SchoolAdmin",backref="school",lazy=True,cascade="all, delete-orphan")
    classes = db.relationship("Class",backref="school",lazy=True,cascade="all, delete-orphan")
    teachers = db.relationship("Teacher",backref="school",lazy=True,cascade="all, delete-orphan")
    students = db.relationship("Student",backref="school",lazy=True,cascade="all, delete-orphan")
    subject= db.relationship("Subject",backref="school",lazy=True,cascade="all, delete-orphan")
    parent= db.relationship("Parent",backref="school",lazy=True,cascade="all, delete-orphan")


    def __repr__(self):
        return f"<School {self.school_name}>"