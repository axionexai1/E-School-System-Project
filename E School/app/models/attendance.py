from datetime import datetime
from app.extensions import db


class Attendance(db.Model):
    __tablename__ = "attendances"

    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"),nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    attendance_date = db.Column(db.Date,nullable=False)
    status = db.Column(db.String(20),nullable=False,default="Present")
    remarks = db.Column(db.String(255),nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    student = db.relationship("Student",backref=db.backref("attendances",lazy=True,cascade="all, delete-orphan"))
    teacher = db.relationship("Teacher",backref=db.backref("marked_attendances",lazy=True))
    classroom = db.relationship("Class",backref=db.backref("attendances",lazy=True))
    section = db.relationship("Section",backref=db.backref("attendances",lazy=True))
    __table_args__ = (db.UniqueConstraint("student_id","attendance_date",name="uq_student_attendance"),)

    def __repr__(self):
        return (f"<Attendance Student={self.student_id} "f"Date={self.attendance_date} "f"Status={self.status}>")