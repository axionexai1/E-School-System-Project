from datetime import datetime
from app.extensions import db


class Subject(db.Model):
    __tablename__ = "subjects"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(db.Integer, primary_key=True)

    # ---------------------------------
    # Relationships
    # ---------------------------------

    # School
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    # Class
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    #Teacher
    teacher= db.relationship("Teacher",backref="subject",lazy=True)
    # ---------------------------------
    # Subject Information
    # ---------------------------------

    subject_name = db.Column(db.String(100),nullable=False)
    subject_code = db.Column(db.String(20),unique=True,nullable=False)
    description = db.Column(db.Text,nullable=True)
    credit_hours = db.Column(db.Integer,nullable=True)

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
        return f"<Subject {self.subject_name}>"