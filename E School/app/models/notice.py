from datetime import datetime
from app.extensions import db


class Notice(db.Model):
    __tablename__ = "notices"

    id = db.Column(db.Integer,primary_key=True)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)
    school_admin_id = db.Column(db.Integer,db.ForeignKey("school_admins.id"),nullable=False)
    title = db.Column(db.String(200),nullable=False)
    description = db.Column(db.Text,nullable=False)
    audience = db.Column(db.String(50),nullable=False,default="All")
    publish_date = db.Column(db.Date,nullable=False)
    expiry_date = db.Column(db.Date,nullable=True)
    attachment = db.Column(db.String(255),nullable=True)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    school = db.relationship("School",back_populates="notices",lazy=True)
    school_admin = db.relationship("SchoolAdmin",backref=db.backref("notices",lazy=True,cascade="all, delete-orphan"))
    def __repr__(self):
        return f"<Notice {self.title}>"