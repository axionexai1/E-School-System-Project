from datetime import datetime
from app.extensions import db


class ParentStudent(db.Model):
    __tablename__ = "parent_students"

    # ---------------------------------
    # Primary Key
    # ---------------------------------

    id = db.Column(db.Integer, primary_key=True)

    # ---------------------------------
    # Foreign Keys
    # ---------------------------------

    parent_id = db.Column(db.Integer,db.ForeignKey("parents.id"),nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"),nullable=False)
    # ---------------------------------
    # Relationship Information
    # ---------------------------------

    relationship = db.Column(db.String(50),nullable=False)
    is_primary_guardian = db.Column(db.Boolean,default=False)
    # ---------------------------------
    # Timestamps
    # ---------------------------------

    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<ParentStudent Parent:{self.parent_id} Student:{self.student_id}>"