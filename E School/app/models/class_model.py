from datetime import datetime
from app.extensions import db


class Class(db.Model):
    __tablename__ = "classes"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(db.Integer, primary_key=True)
    # School Relationship
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    # Class Information
    class_name = db.Column(db.String(100),nullable=False)
    class_code = db.Column(db.String(20),nullable=False)
    description = db.Column(db.Text,nullable=True)
    # ---------------------------------
    # Class Teacher (Optional)
    # Will be connected after Teacher model
    # ---------------------------------
    class_teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=True)

    # Status
    is_active = db.Column(db.Boolean,default=True)

    # Timestamps
    # ---------------------------------
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    # Relationships
    # ---------------------------------
    sections = db.relationship("Section",backref="class_room",lazy=True,cascade="all, delete-orphan")
    students = db.relationship("Student",backref="class_room",lazy=True,cascade="all, delete-orphan")
    subjects = db.relationship("Subject",backref="class_room",lazy=True,cascade="all, delete-orphan")
    teacher = db.relationship("Teacher",foreign_keys=[class_teacher_id],backref="managed_classes")

    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Class {self.class_name}>"