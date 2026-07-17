from datetime import datetime
from app.extensions import db


class AssignmentSubmission(db.Model):
    __tablename__ = "assignment_submissions"

    id = db.Column(db.Integer,primary_key=True)
    assignment_id = db.Column(db.Integer,db.ForeignKey("assignments.id"),nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"),nullable=False)
    submission_date = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    submitted_file = db.Column(db.String(255),nullable=True)
    remarks = db.Column(db.Text,nullable=True)
    marks_obtained = db.Column(db.Float,nullable=True)
    teacher_feedback = db.Column(db.Text,nullable=True)
    submission_status = db.Column(db.String(30),default="Submitted",nullable=False)
    is_late_submission = db.Column(db.Boolean,default=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    assignment = db.relationship("Assignment",backref=db.backref("submissions",lazy=True,cascade="all, delete-orphan"))
    student = db.relationship("Student",backref=db.backref("assignment_submissions",lazy=True,cascade="all, delete-orphan"))
    __table_args__ = (db.UniqueConstraint("assignment_id","student_id",name="uq_assignment_submission"),)
    def __repr__(self):
        return (f"<AssignmentSubmission "f"Assignment={self.assignment_id}, "f"Student={self.student_id}>")