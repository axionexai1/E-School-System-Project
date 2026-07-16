from datetime import datetime
from app.extensions import db


class FeeStructure(db.Model):
    __tablename__ = "fee_structures"

    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    academic_year = db.Column(db.String(20),nullable=False)
    fee_type = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Numeric(10, 2),nullable=False)
    due_day = db.Column(db.Integer,nullable=True)
    description = db.Column(db.Text,nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",backref=db.backref("fee_structures",lazy=True,cascade="all, delete-orphan"))
    classroom = db.relationship("Class",backref=db.backref("fee_structures",lazy=True,cascade="all, delete-orphan"))
    __table_args__ = (db.UniqueConstraint("class_id","fee_type","academic_year",name="uq_fee_structure"),)
    def __repr__(self):
        return f"<FeeStructure {self.fee_type}>"
