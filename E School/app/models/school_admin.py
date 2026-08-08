from datetime import datetime
from app.extensions import db


class SchoolAdmin(db.Model):
    __tablename__ = "school_admins"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False,unique=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    employee_id = db.Column(db.String(20),unique=True,nullable=False)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    gender = db.Column(db.String(20),nullable=True)
    date_of_birth = db.Column(db.Date,nullable=True)
    address = db.Column(db.String(255),nullable=True)
    profile_image = db.Column(db.String(255),nullable=True)
    designation = db.Column(db.String(100),default="School Administrator")
    joining_date = db.Column(db.Date,nullable=True)
    salary = db.Column(db.Numeric(10, 2),nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School", back_populates ="school_admins")
    user = db.relationship("User", back_populates = "school_admin", uselist = False)

    def __repr__(self):
        return f"<SchoolAdmin {self.employee_id}>"