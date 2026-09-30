from datetime import datetime
from app.extensions import db


class Assignment(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    title = db.Column(db.String(200),nullable=False)
    description = db.Column(db.Text,nullable=False)
    total_marks = db.Column(db.Integer,nullable=False)
    assigned_date = db.Column(db.Date,nullable=False)
    due_date = db.Column(db.Date,nullable=False)
    attachment = db.Column(db.String(255),nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",backref=db.backref("assignments",lazy=True))
    teacher = db.relationship("Teacher",back_populates="assignments")
    subject = db.relationship("Subject",back_populates="assignments")
    class_room = db.relationship("Class",back_populates="assignments")
    sections = db.relationship("Section",back_populates="assignments")
    submissions = db.relationship("AssignmentSubmission",back_populates="assignments")
    def __repr__(self):
        return f"<Assignment {self.title}>"
