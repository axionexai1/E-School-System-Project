from datetime import datetime
from app.extensions import db


class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"),nullable=False)
    exam_id = db.Column(db.Integer,db.ForeignKey("exams.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    obtained_marks = db.Column(db.Float,nullable=False)
    grade = db.Column(db.String(5),nullable=True)
    remarks = db.Column(db.String(255),nullable=True)
    is_pass = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    students = db.relationship("Student",back_populates="results",lazy=True)
    exams = db.relationship("Exam",back_populates="results",lazy=True)
    subject = db.relationship("Subject",back_populates="results",lazy=True)
    teacher = db.relationship("Teacher",back_populates="results",lazy=True)
    class_room = db.relationship("Class",back_populates="results",lazy=True)
    section = db.relationship("Section",back_populates="results",lazy=True)
    __table_args__ = (db.UniqueConstraint("student_id","exam_id","subject_id",name="uq_student_exam_result"),)
    def __repr__(self):
        return (f"<Result Student={self.student_id}, "f"Exam={self.exam_id}, "f"Marks={self.obtained_marks}>")
