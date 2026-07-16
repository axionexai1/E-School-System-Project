from datetime import datetime
from app.extensions import db


class Exam(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    exam_name = db.Column(db.String(100),nullable=False)
    exam_type = db.Column(db.String(50),nullable=False)
    exam_date = db.Column(db.Date,nullable=False)
    start_time = db.Column(db.Time,nullable=True)
    end_time = db.Column(db.Time,nullable=True)
    total_marks = db.Column(db.Integer,nullable=False)
    passing_marks = db.Column(db.Integer,nullable=False)
    academic_year = db.Column(db.String(20),nullable=False)
    instructions = db.Column(db.Text,nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",backref=db.backref("exams",lazy=True))
    subject = db.relationship("Subject",backref=db.backref("exams",lazy=True))
    classroom = db.relationship("Class",backref=db.backref("exams",lazy=True))
    section = db.relationship("Section",backref=db.backref("exams",lazy=True))
    teacher = db.relationship("Teacher",backref=db.backref("exams",lazy=True))
    __table_args__ = (db.UniqueConstraint("exam_name","subject_id","class_id","section_id","academic_year",name="uq_exam_schedule"),)
    def __repr__(self):
        return f"<Exam {self.exam_name}>"
