
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.extensions import db
from .forms import CreateSchoolForm
from app.models.school import School
from flask_login import logout_user
from sqlalchemy.exc import IntegrityError
from .forms import EditSchoolForm

from . import software_admin



@software_admin.route("/dashboard")
@login_required
def dashboard():
    return render_template("software_admin/dashboard.html")


@software_admin.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.login"))


# ===========================
# School Management
# ===========================
@software_admin.route("/school/<int:school_id>/detail")
@login_required
def school_detail(school_id):

    school = School.query.get_or_404(school_id)

    student_count = 0
    teacher_count = 0
    class_count = 0
    subscription = "Basic Plan"

    return render_template("software_admin/school_detail.html",
    school=school,
    student_count=student_count,
    teacher_count=teacher_count,
    class_count=class_count,
    subscription=subscription
    )



@software_admin.route("/schools/list")
@login_required
def schools():
    schools = School.query.all()
    return render_template("software_admin/schools.html", schools=schools)

@software_admin.route('/schools')
@login_required
def manage_schools():
    print("MANAGE SCHOOLS ROUTE OPENED")
    schools = School.query.all()
    print("Number of Schools: ", len(schools))

    for s in schools:
        print(s.school_name,s.school_code)


    return render_template("software_admin/manage_schools.html", schools=schools)



@software_admin.route("/schools/create", methods=["GET", "POST"])
@login_required
def create_school():

    form = CreateSchoolForm()

    if form.validate_on_submit():
        existing_school = School.query.filter_by(school_code=form.school_code.data).first()
        if existing_school:
            flash("School code already Exist. Please use another code.", "danger")
            return render_template('software_admin/create_school.html', form=form)
        school = School(
            school_name=form.school_name.data,
            school_code=form.school_code.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            city = form.city.data,
            country = form.country.data
            )
        try:
            db.session.add(school)
            db.session.commit()
            print("Saved: ",school.school_name)
            flash("School created successfully!", "success")
            return redirect(url_for("software_admin.manage_schools"))
        except IntegrityError:
            db.session.rollback()
            flash("Something went wrong. Please try again.", "danger")


    return render_template("software_admin/create_school.html",form=form)


#Route For Edit School:
@software_admin.route("/schools/<int:id>/edit", methods=["GET","POST"])
@login_required
def edit_school(id):

    school = School.query.get_or_404(id)
    form = EditSchoolForm(obj=school)
    if form.validate_on_submit():

        school.school_name = form.school_name.data
        school.school_code = form.school_code.data
        school.email = form.email.data
        school.phone = form.phone.data
        school.address = form.address.data
        school.city = form.city.data
        school.country = form.country.data

        db.session.commit()

        flash("School updated successfully!", "success")

        return redirect(url_for("software_admin.school_detail",school_id=school.id))

    return render_template("software_admin/edit_school.html",form=form,school=school)


    
#For Delete School

@software_admin.route("/schools/<int:id>/delete", methods =["POST"])
@login_required
def delete_school(id):
    school = School.query.get_or_404(id)

    db.session.delete(school)
    db.session.commit()

    flash(" School deleted successfully.", "success")
    return redirect(url_for("software_admin.schools"))
    


# ===========================
# School Admin Management
# ===========================

@software_admin.route("/school-admins")
@login_required
def school_admins():
    return render_template("software_admin/school_admins.html")


@software_admin.route("/school-admins/create")
@login_required
def create_school_admin():
    return render_template("software_admin/create_school_admin.html")


@software_admin.route("/school-admins/<int:id>/edit")
@login_required
def edit_school_admin(id):
    return render_template("software_admin/edit_school_admin.html")


@software_admin.route("/school-admins/<int:id>/delete")
@login_required
def delete_school_admin(id):
    pass


# ===========================
# Subscription Management
# ===========================

@software_admin.route("/subscriptions")
@login_required
def subscriptions():
    return render_template("software_admin/subscriptions.html")


# ===========================
# Package Management
# ===========================

@software_admin.route("/packages")
@login_required
def packages():
    return render_template("software_admin/packages.html")


# ===========================
# System Settings
# ===========================

@software_admin.route("/settings")
@login_required
def settings():
    return render_template("software_admin/settings.html")


# ===========================
# Profile
# ===========================

@software_admin.route("/profile")
@login_required
def profile():
    return render_template("software_admin/profile.html")