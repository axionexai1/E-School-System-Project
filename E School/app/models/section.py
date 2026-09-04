from datetime import datetime
from app.extensions import db


class Section(db.Model):
    __tablename__ = "sections"

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

    # Section Information
    # ---------------------------------
    section_name = db.Column(db.String(20),nullable=False)
    section_code = db.Column(db.String(20),nullable=False)
    description = db.Column(db.Text,nullable=True)
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
    # Relationships
    # ---------------------------------
    school = db.relationship("School",back_populates="sections")
    class_room = db.relationship("Class",back_populates="sections")
    exams = db.relationship("Exam",back_populates="sections")
    timetables = db.relationship("Timetable",back_populates="section",cascade="all, delete-orphan")
    assignments = db.relationship("Assignment",back_populates="sections",cascade="all, delete-orphan")
    teacher_subjects = db.relationship("TeacherSubject", back_populates = "section", cascade="all, delete-orphan")
    students = db.relationship("Student",back_populates="section",cascade="all, delete-orphan")
    results = db.relationship("Result",back_populates="section",cascade="all, delete-orphan")

    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Section {self.section_name}>"
