from datetime import datetime
from app.extensions import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50),unique=True,nullable=False)
    description = db.Column(db.String(255),nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

# Relationship with User model
    users = db.relationship("User",back_populates="role")

    def __repr__(self):
        return f"<Role {self.role_name}>"