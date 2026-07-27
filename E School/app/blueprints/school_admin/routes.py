from flask import render_template
from flask_login import login_required, current_user
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.class_model import Class
from app.models.section import Section 
from app.models.subject import Subject
from . import school_admin


@school_admin.route("/dashboard")
@login_required
def dashboard():

    total_students = Student.query.filter_by(school_id=current_user.school_id).count()

    total_teachers = Teacher.query.filter_by(
    school_id=current_user.school_id
    ).count()

    total_classes = Class.query.filter_by(
    school_id=current_user.school_id
    ).count()

    total_sections = Section.query.filter_by(
    school_id=current_user.school_id
    ).count()

    total_subjects = Subject.query.filter_by(
    school_id=current_user.school_id
    ).count()

    pending_fees = 0

    return render_template(
    "school_admin/dashboard.html",
    total_students=total_students,
    total_teachers=total_teachers,
    total_classes=total_classes,
    total_sections=total_sections,
    total_subjects=total_subjects,
    pending_fees=pending_fees,
    )

   