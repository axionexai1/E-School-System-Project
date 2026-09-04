from datetime import datetime
from app.extensions import db


class FeePayment(db.Model):
    __tablename__ = "fee_payments"

    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"),nullable=False)
    fee_structure_id = db.Column(db.Integer,db.ForeignKey("fee_structures.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    school_admin_id = db.Column(db.Integer,db.ForeignKey("school_admins.id"),nullable=False)
    amount_paid = db.Column(db.Numeric(10, 2),nullable=False)
    payment_date = db.Column(db.Date,nullable=False)
    payment_method = db.Column(db.String(50),nullable=False)
    transaction_id = db.Column(db.String(100),unique=True,nullable=True)
    receipt_number = db.Column(db.String(100),unique=True,nullable=False)
    payment_status = db.Column(db.String(20),default="Paid")
    remarks = db.Column(db.Text,nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    student = db.relationship("Student",back_populates="fee_payments")
    fee_structure =db.relationship("FeeStructure",back_populates="fee_payments")
    classroom = db.relationship("Class",backref=db.backref("fee_payments",lazy=True))
    school_admin = db.relationship("SchoolAdmin",backref=db.backref("fee_payments",lazy=True))
    def __repr__(self):
        return (f"<FeePayment "f"Receipt={self.receipt_number} "f"Student={self.student_id}>")