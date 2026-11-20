
from flask import render_template
from flask_login import login_required, current_user
from app.models.teacher import Teacher
from app.models import Timetable
from app.models.teacher_subject import TeacherSubject

from . import teachers


@teachers.route("/dashboard")
@login_required
def dashboard():

    teacher = Teacher.query.filter_by(
    user_id=current_user.id,
    school_id=current_user.school_id
    ).first_or_404()

    assignments = TeacherSubject.query.filter_by(
    teacher_id=teacher.id,
    school_id=current_user.school_id,
    is_active=True
    ).all()

    total_subjects = len({
    a.subject_id for a in assignments
    })

    total_classes = len({
    a.class_id for a in assignments
    })

    return render_template(
    "teachers/dashboard.html",
    teacher=teacher,
    total_subjects=total_subjects,
    total_classes=total_classes
    )
# ------- My Time Table --------

@teachers.route("/my-timetable")
@login_required
def my_timetable():

    teacher_record = Teacher.query.filter_by(
    user_id=current_user.id,
    school_id=current_user.school_id
    ).first_or_404()

    timetables = Timetable.query.filter_by(
    teacher_id=teacher_record.id,
    school_id=current_user.school_id,
    is_active=True
    ).order_by(
    Timetable.day_of_week,
    Timetable.start_time
    ).all()

    return render_template(
    "teachers/timetable/my_timetable.html",
    teacher=teacher_record,
    timetables=timetables
    )

# ------- My Subject --------
@teachers.route("/my-subjects")
@login_required
def my_subjects():

    # Get the logged-in teacher
    teacher = Teacher.query.filter_by(
    user_id=current_user.id,
    school_id=current_user.school_id
    ).first_or_404()

    # Get subjects assigned to this teacher
    assignments = TeacherSubject.query.filter_by(
    teacher_id=teacher.id,
    school_id=current_user.school_id,
    is_active=True
    ).all()

    return render_template(
    "teachers/subjects/my_subjects.html",
    teacher=teacher,
    assignments=assignments
    )


# -------- My Classes --------

@teachers.route("/my-classes")
@login_required
def my_classes():

    # Step 1: Find the logged-in teacher
    teacher = Teacher.query.filter_by(
    user_id=current_user.id,
    school_id=current_user.school_id
    ).first_or_404()

    # Step 2: Get this teacher's active assignments
    assignments = TeacherSubject.query.filter_by(
    teacher_id=teacher.id,
    school_id=current_user.school_id,
    is_active=True
    ).all()

    # Step 3: Count unique assigned classes
    total_classes = len({
    assignment.class_id for assignment in assignments
    })

    # Step 4: Count unique assigned sections
    total_sections = len({
    (assignment.class_id, assignment.section_id)
    for assignment in assignments
    })

    return render_template(
    "teachers/classes/my_classes.html",
    teacher=teacher,
    assignments=assignments,
    total_classes=total_classes,
    total_sections=total_sections
    )
