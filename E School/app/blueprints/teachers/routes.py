from flask import render_template
from flask_login import login_required, current_user
from app.models.teacher import Teacher
from . import teachers


@teachers.route("/dashboard")
@login_required
def dashboard():

    teacher = Teacher.query.filter_by(user_id=current_user.id).first_or_404()

    return render_template(
    "teachers/dashboard.html",
    teacher=teacher
    )
