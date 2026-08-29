from flask import render_template
from flask_login import login_required, current_user
from app.models.student import Student
from . import student


@student.route("/dashboard")
@login_required
def dashboard():

    student = Student.query.filter_by(user_id=current_user.id).first_or_404()

    if not student:
        return "Student profile not found for this account.", 404
    return render_template(
    "student/dashboard.html",
    student=student
    )

