from datetime import datetime
from app.extensions import db


class Teacher(db.Model):
    __tablename__ = "teachers"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), nullable=False)
 
  

    # Personal Information
    employee_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    cnic = db.Column(db.String(20), unique=True, nullable=True)
    address = db.Column(db.String(255), nullable=True)
    emergency_contact = db.Column(db.String(20), nullable=True)
    blood_group = db.Column(db.String(5), nullable=True)

    # Professional Information
    qualification = db.Column(db.String(150), nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    joining_date = db.Column(db.Date, nullable=True)
    salary = db.Column(db.Numeric(10, 2), nullable=True)
    profile_image = db.Column(db.String(255), nullable=True)
    employment_status = db.Column(
    db.String(20),default="Active")
    notes = db.Column(db.Text, nullable=True)
    # Status
    is_active = db.Column(db.Boolean, default=True)
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
    db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # Relationships
    user= db.relationship("User", back_populates= "teacher", uselist= False)
    teacher_subjects = db.relationship("TeacherSubject", back_populates ="teacher", cascade= "all, delete-orphan",lazy= True)
    school = db.relationship("School", back_populates="teachers")
   
 

    def __repr__(self):
        return f"<Teacher {self.employee_number} - {self.first_name} {self.last_name}>"