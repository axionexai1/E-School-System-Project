from datetime import datetime
from app.extensions import db


class Parent(db.Model):
    __tablename__ = "parents"

# ---------------------------------
# Primary Key
# ---------------------------------

    id = db.Column(db.Integer, primary_key=True)

# ---------------------------------
# Foreign Keys
# ---------------------------------

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False,unique=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    # ---------------------------------
    # Parent Information
    # ---------------------------------
    father_name = db.Column(db.String(100),nullable=False)
    mother_name = db.Column(db.String(100),nullable=True)
    guardian_name = db.Column(db.String(100),nullable=True)
    relationship = db.Column(db.String(50),nullable=True)
    phone = db.Column(db.String(20),nullable=False)
    alternate_phone = db.Column(db.String(20),nullable=True)
    email = db.Column(db.String(120),nullable=True)
    occupation = db.Column(db.String(100),nullable=True)
    address = db.Column(db.String(255),nullable=True)
    profile_image = db.Column(db.String(255),nullable=True)
    # ---------------------------------
    # Status
    # ---------------------------------
    is_active = db.Column(db.Boolean,default=True)
    # ---------------------------------
    #RelationShip
    students=db.relationship("ParentStudent",backref="parent",lazy=True,cascade="all, delete-orphan")
    # Timestamps
    # ---------------------------------
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    # ---------------------------------
    # String Representation
    # ---------------------------------

    def __repr__(self):
        return f"<Parent {self.father_name}>"