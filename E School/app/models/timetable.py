from datetime import datetime
from app.extensions import db


class Timetable(db.Model):
    __tablename__ = "timetables"

    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"),nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"),nullable=False)
    day_of_week = db.Column(db.String(20),nullable=False)
    start_time = db.Column(db.Time,nullable=False)
    end_time = db.Column(db.Time,nullable=False)
    room_number = db.Column(db.String(20),nullable=True)
    academic_year = db.Column(db.String(20),nullable=False)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",backref=db.backref("timetables",lazy=True))
    classroom = db.relationship("Class",backref=db.backref("timetables",lazy=True))
    section = db.relationship("Section",backref=db.backref("timetables",lazy=True))
    subject = db.relationship("Subject",backref=db.backref("timetables",lazy=True))
    teacher = db.relationship("Teacher",backref=db.backref("timetables",lazy=True))
    __table_args__ = (db.UniqueConstraint("class_id","section_id","day_of_week","start_time",name="uq_class_timetable"),)

    def __repr__(self):
        return (f"<Timetable "f"{self.day_of_week} "f"{self.start_time}-{self.end_time}>")
