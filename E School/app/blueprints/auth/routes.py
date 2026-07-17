from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import bcrypt
from app.forms.login_form import LoginForm
from app.models.user import User
from . import auth


@auth.route("/")
def home():
    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect_dashboard(current_user)

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            if bcrypt.check_password_hash(user.password_hash, password):
                if not user.is_active:
                    flash("Your account has been deactivated.","warning")
                    return redirect(url_for("auth.login"))

                login_user(user)
                flash("Login successful.","success")
                return redirect_dashboard(user)
        flash("Invalid email or password.","danger")
    return render_template("auth/login.html",form=form)


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("You have been logged out successfully.","success")
    return redirect(url_for("auth.login"))


def redirect_dashboard(user):

    role = user.role.role_name.strip().lower()

    if role == "software admin":
        return redirect(url_for("software_admin.dashboard"))

    elif role == "school admin":
        return redirect(url_for("school_admin.dashboard"))

    elif role == "teacher":
        return redirect(url_for("teacher.dashboard"))

    elif role == "student":
        return redirect(url_for("student.dashboard"))

    elif role == "parent":
        return redirect(url_for("parent.dashboard"))

    flash("No dashboard is assigned to your account.","danger")
    logout_user()

    return redirect(url_for("auth.login"))