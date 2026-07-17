from collections import UserList
from datetime import datetime
from flask_login import UserMixin
from app.extensions import db, bcrypt, login_manager



class User(UserMixin, db.Model):
    __tablename__ = "users"

    # -------------------------
    # Primary Key
    # -------------------------
    id = db.Column(db.Integer, primary_key=True)
    #Full Name
    full_name = db.Column(db.String(100), nullable=False)
    # Role Relationship
    # -------------------------
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"),nullable=False)
    # -------------------------
    #Relationship
    student=db.relationship("Student",backref="user",uselist=False,cascade="all, delete-orphan")
    teacher=db.relationship("Teacher",backref="user",uselist=False,cascade="all, delete-orphan")
    parent= db.relationship("Parent",backref="user",uselist=False,cascade="all, delete-orphan")
    # School Relationship
    # Software Admin does not belong to a school,
    # so school_id can be NULL.
    # -------------------------
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=True)
    # -------------------------
    # Login Information
    # -------------------------
    username = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)
    # -------------------------
    # Account Status
    # -------------------------
    is_active = db.Column(db.Boolean,default=True)
    is_verified = db.Column(db.Boolean,default=False)
    last_login = db.Column(db.DateTime,nullable=True)\
    # -------------------------
    # Timestamps
    # -------------------------
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # -------------------------
    # Password Methods
    # -------------------------
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # -------------------------
    # String Representation
    # -------------------------
    def __repr__(self):
        return f"<User {self.username}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))