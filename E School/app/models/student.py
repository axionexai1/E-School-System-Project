from datetime import datetime
from app.extensions import db

# Student Parent Association Table:
student_parent = db.Table("student_parent", db.Column("student_id", 
db.Integer, db.ForeignKey("students.id", ondelete="CASCADE"), primary_key=True), 
db.Column("parent_id", db.Integer, db.ForeignKey("parents.id", ondelete="CASCADE"),primary_key =True ))


class Student(db.Model):
    __tablename__ = "students"

    # ---------------------------------
    # Primary Key
    # ---------------------------------
    id = db.Column(db.Integer, primary_key=True)

    # ---------------------------------
    #relationship
    user = db.relationship("User", back_populates = "student")
    school = db.relationship("School",back_populates="students")
    class_room = db.relationship("Class",back_populates="students")
    section = db.relationship("Section",back_populates="students")
    assignment_submissions= db.relationship("AssignmentSubmission",back_populates="students")
    attendances = db.relationship("Attendance",back_populates="students",cascade="all, delete-orphan")
    results = db.relationship("Result",back_populates="students")
    fee_payments = db.relationship("FeePayment",back_populates="student")
    # Foreign Keys
    # ---------------------------------
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False,unique=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("classes.id"),nullable=False)
    section_id = db.Column(db.Integer,db.ForeignKey("sections.id"),nullable=False)

    # ---------------------------------
    # Student Information
    # ---------------------------------

    admission_number = db.Column(db.String(30),unique=True,nullable=False)
    roll_number = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    date_of_birth = db.Column(db.Date,nullable=False)
    admission_date = db.Column(db.Date,nullable=False)
    phone = db.Column(db.String(20),nullable=True)
    address = db.Column(db.String(255),nullable=True)
    profile_image = db.Column(db.String(255),nullable=True)
    blood_group = db.Column(db.String(10),nullable=True)
    guardian_name = db.Column(db.String(100),nullable=True)
    guardian_phone=db.Column(db.String(30),nullable=True)
    cnic = db.Column(db.String(30),nullable=True)
    # ---------------------------------
    # Status
    # ---------------------------------

    is_active = db.Column(db.Boolean,default=True)
    # ---------------------------------
    # Timestamps
    # ---------------------------------

    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"