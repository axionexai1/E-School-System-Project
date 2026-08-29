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
    teacher_subjects = db.relationship("TeacherSubject", back_populates = "classroom", cascade= "all, delete-orphan",lazy= True)  
    sections = db.relationship("Section",back_populates= "class_room",cascade="all, delete-orphan")
    students = db.relationship("Student", back_populates= "class_room")
    results=   db.relationship("Result", back_populates= "class_room")
    exams = db.relationship("Exam", back_populates= "class_room",cascade="all, delete-orphan")
    timetables = db.relationship("Timetable",back_populates= "class_room",cascade="all, delete-orphan")
    assignments = db.relationship("Assignment",back_populates= "class_room",cascade="all, delete-orphan")
    fee_structures = db.relationship("FeeStructure",back_populates= "class_room",cascade="all, delete-orphan")
    class_teacher = db.relationship("Teacher",foreign_keys=[class_teacher_id],back_populates="managed_class", uselist=False )
    school = db.relationship("School",back_populates="classes")
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Class {self.class_name}>"