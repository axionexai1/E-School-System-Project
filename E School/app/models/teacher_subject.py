from datetime import datetime
from app.extensions import db


class TeacherSubject(db.Model):
    __tablename__ = "teacher_subjects"

    id = db.Column(db.Integer,primary_key=True)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    academic_year = db.Column(db.String(20),nullable=False)
    is_class_teacher = db.Column(db.Boolean,default=False)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",back_populates="teacher_subjects")
    teacher = db.relationship("Teacher",back_populates="teacher_subjects")
    subject = db.relationship("Subject",back_populates="teacher_subjects")
    classroom = db.relationship("Class",back_populates="teacher_subjects")
    section = db.relationship("Section",back_populates="teacher_subjects")
    __table_args__ = (db.UniqueConstraint("teacher_id","subject_id","class_id","section_id","academic_year",name="uq_teacher_subject_assignment"),)
    def __repr__(self):
        return (f"<TeacherSubject "f"Teacher={self.teacher_id}, "f"Subject={self.subject_id}>")
