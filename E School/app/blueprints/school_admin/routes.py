from app.extensions import db
from app.extensions import bcrypt
from flask import render_template, redirect,url_for, flash, request
from flask_login import login_required, current_user
from app.models.student import Student
from app.models.teacher_subject import TeacherSubject
from app.models.teacher import Teacher
from app.models.class_model import Class
from app.models.section import Section 
from app.models.subject import Subject
from app.models.user import User
from app.models.role import Role
from app.models.student import Student
from sqlalchemy import or_
from . import school_admin
from .forms import ClassForm
from .forms import SectionForm
from .forms import StudentForm
from .forms import TeacherForm
from .forms import TeacherSubjectForm
from .forms import SubjectForm
import secrets
@school_admin.route("/dashboard")
@login_required
def dashboard():

    total_students = Student.query.filter_by(school_id=current_user.school_id).count()

    total_teachers = Teacher.query.filter_by(school_id=current_user.school_id).count()
    total_classes = Class.query.filter_by(school_id=current_user.school_id).count()
    total_sections = Section.query.filter_by(school_id=current_user.school_id).count()
    total_subjects = Subject.query.filter_by(school_id=current_user.school_id).count()
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
#------------------------
# Classes Management
#______________________------

@school_admin.route("/classes")
@login_required
def manage_classes():

    classes = Class.query.filter_by(school_id=current_user.school_id).order_by(Class.class_name).all()
    return render_template("school_admin/manage_classes.html",classes=classes)

@school_admin.route("/classes/create", methods=["GET", "POST"])
@login_required
def create_class():

    form = ClassForm()

    if form.validate_on_submit():

        existing = Class.query.filter_by(
    school_id=current_user.school_id,
    class_name=form.class_name.data
    ).first()

        if existing:

            flash("Class already exists.","warning")

            return redirect(url_for("school_admin.create_class"))

        new_class = Class(class_name=form.class_name.data,class_code= form.class_code.data,description=form.description.data,
        school_id=current_user.school_id)

        db.session.add(new_class)
        db.session.commit()

        flash("Class created successfully.","success")

        return redirect(
    url_for("school_admin.manage_classes")
    )

    return render_template("school_admin/create_class.html",form=form)


@school_admin.route("/classes/<int:id>")
@login_required
def class_detail(id):

    class_obj = Class.query.filter_by(id=id,school_id=current_user.school_id).first_or_404()

    return render_template("school_admin/class_detail.html",class_obj=class_obj)

@school_admin.route("/classes/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_class(id):

    class_obj = Class.query.filter_by(
    id=id,school_id=current_user.school_id).first_or_404()

    form = ClassForm(obj=class_obj)

    if form.validate_on_submit():

        class_obj.class_name = form.class_name.data
        class_obj.class_code = form.class_code.data
        class_obj.description = form.description.data

        db.session.commit()

        flash("Class updated successfully.","success")

        return redirect(url_for("school_admin.manage_classes"))

    return render_template("school_admin/edit_class.html",form=form,class_obj=class_obj)



@school_admin.route("/classes/<int:id>/delete", methods=["POST"])
@login_required
def delete_class(id):

    class_obj = Class.query.filter_by(
    id=id,school_id=current_user.school_id).first_or_404()

    db.session.delete(class_obj)
    db.session.commit()

    flash("Class deleted successfully.""success")

    return redirect(url_for("school_admin.manage_classes"))
    



# -------------------------------------------
#   ------ Section Management ----------------
# ---------------------------------------------
 # For  Manage Section

@school_admin.route("/manage-sections")
@login_required
def manage_sections():

    sections = Section.query.filter_by(school_id=current_user.school_id).all()
    return render_template(
    "school_admin/manage_sections.html",
    sections=sections
    )

# For Creating Section

@school_admin.route("/create-section", methods=["GET", "POST"])
@login_required
def create_section():

    form = SectionForm()

    classes = Class.query.filter_by(school_id=current_user.school_id,is_active=True).all()
    form.class_id.choices = [(c.id, c.class_name) for c in classes]

    if form.validate_on_submit():

        section = Section(class_id=form.class_id.data,section_name=form.section_name.data,section_code=form.section_code.data,
        description=form.description.data,
        school_id=current_user.school_id
        )

        db.session.add(section)
        db.session.commit()

        flash("Section created successfully!", "success")

        return redirect(
        url_for("school_admin.manage_sections")
        )

    return render_template(
    "school_admin/create_section.html",
    form=form
    )


# For Section Detail 

@school_admin.route("/section/<int:id>")
@login_required
def section_detail(id):

    section = Section.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()

    return render_template(
    "school_admin/section_detail.html",
    section=section
    )

# For Edit Section 

@school_admin.route("/section/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_section(id):

    section = Section.query.filter_by(id=id,school_id=current_user.school_id).first_or_404()
    form = SectionForm(obj=section)

    classes = Class.query.filter_by(school_id=current_user.school_id,is_active=True).all()
    form.class_id.choices = [(c.id, c.class_name) for c in classes]

    if form.validate_on_submit():

        section.class_id = form.class_id.data
        section.section_name = form.section_name.data
        section.description = form.description.data

        db.session.commit()

        flash("Section updated successfully!", "success")

        return redirect(
        url_for("school_admin.manage_sections")
        )

    return render_template(
    "school_admin/edit_section.html",
    form=form,
    section=section
    )

# For Delete Section

@school_admin.route("/section/<int:id>/delete", methods=["POST"])
@login_required
def delete_section(id):

    section = Section.query.filter_by(id=id,school_id=current_user.school_id).first_or_404()

    db.session.delete(section)
    db.session.commit()

    flash("Section deleted successfully!", "success")

    return redirect(
    url_for("school_admin.manage_sections"))


# For Teacher Management System
# Manage Teacher

@school_admin.route("/manage-teachers")
@login_required
def manage_teachers():

    teachers = Teacher.query.filter_by(school_id=current_user.school_id).order_by(Teacher.created_at.desc()).all()

    return render_template("school_admin/manage_teachers.html",teachers=teachers)


@school_admin.route("/create-teacher", methods=["GET", "POST"])
@login_required
def create_teacher():

    form = TeacherForm()

    # -------------------------
    # Load Managed Class Dropdown
    # -------------------------
    classes = Class.query.filter_by(is_active=True).all()

    form.managed_class_id.choices = [(0, "-- Select Class --")]
    form.managed_class_id.choices += [
    (c.id, c.class_name) for c in classes
    ]

    # -------------------------
    # Save Teacher
    # -------------------------
    if request.method == "POST":
        print("POST request recieved")
        print("Form Errors: ", form.errors)
    if form.validate_on_submit():
        print("Step: 1")

        # 1. Find Teacher Role
        teacher_role = Role.query.filter_by(role_name="Teacher").first()
        print("Step: 2")
        if not teacher_role:
            flash("Teacher role not found.", "danger")
            return redirect(url_for("school_admin.manage_teachers"))

        # 2. Generate Teacher ID
        teacher_number = 1

        while Teacher.query.filter_by(school_id =current_user.school_id,employee_number =f"TCH-{teacher_number + 1:04d}").first():
            teacher_number += 1

        teacher_id = f"TCH-{teacher_number + 1:04d}"

        # 3. Generate Username
        username = form.email.data

        # 4. Generate Temporary Password
        temp_password = secrets.token_urlsafe(8)
        print("Step: 3")
        # 5. Create User
        exiting_user = User.query.filter((User.email ==form.email.data)| (User.username == form.email.data)).first()
        if exiting_user:
            flash("A user with this Email already exists.", "danger")
            return render_template("school_admin/create_teacher.html", form= form)
        user = User(
        full_name= f"{form.first_name.data} {form.last_name.data}",
        username=username,
        email=form.email.data,
        role_id=teacher_role.id,
        school_id=current_user.school_id
        )
        print("Step: 4")
        user.set_password(temp_password)

        print("Creating User......")
        db.session.add(user)

        # Get user.id before commit
        db.session.flush()
        print("Step: 5")
        # Managed Class
        managed_class = (
        None
        if form.managed_class_id.data == 0
        else form.managed_class_id.data
        )

        # 6. Create Teacher
        teacher = Teacher(
        user_id=user.id,
        school_id=current_user.school_id,

        employee_number=teacher_id,

        first_name=form.first_name.data,last_name=form.last_name.data,
        email=form.email.data,
        phone=form.phone.data,
        gender=form.gender.data,

        date_of_birth=form.date_of_birth.data,

        qualification=form.qualification.data,
        experience=form.experience.data,

        joining_date=form.joining_date.data,

        address=form.address.data,

        salary=form.salary.data,
        )
        print("Step: 6")
        db.session.add(teacher)
        db.session.flush()

        if form.managed_class_id.data != 0:
            classroom = Class.query.get(form.managed_class_id.data)
            if classroom:
                classroom.class_teacher_id = teacher.id
        # 7. Save Both
        
        db.session.commit()
       
        flash("Teacher created successfully!", "success")
        return render_template("school_admin/teacher_created.html",teacher=teacher, username= username, password= temp_password)
    else:
        print("Validate_on_Submit = False")
        print("Request Method: ", request.method)
        print("Form Errors: ", form.errors)
        print(" CSRF Errors: ")
    return render_template(
    "school_admin/create_teacher.html",
    form=form
    )


# Teacher detail

@school_admin.route("/teacher/<int:id>")
@login_required
def teacher_detail(id):

    teacher = Teacher.query.get_or_404(id)

    return render_template(
    "school_admin/teacher_detail.html",
    teacher=teacher
    )

# For Edit Teacher 

@school_admin.route("/teacher/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_teacher(id):

    teacher = Teacher.query.get_or_404(id)

    form = TeacherForm(obj=teacher)

  
    classes = Class.query.filter_by(is_active=True).all()

    form.managed_class_id.choices = [
    (0, "-- Select Class --")
    ]

    form.managed_class_id.choices += [
    (c.id, c.class_name)
    for c in classes
    ]

    if request.method == "GET":

        managed_class = Class.query.filter_by(class_teacher_id = teacher.id).first()

        if managed_class:
            form.managed_class_id.data = managed_class.id

        else:
            form.managed_class_id.data =0 
        

    if form.validate_on_submit():

            teacher.first_name = form.first_name.data
            teacher.last_name = form.last_name.data
            teacher.email = form.email.data
            teacher.phone = form.phone.data
            teacher.gender = form.gender.data
            teacher.date_of_birth = form.date_of_birth.data
            teacher.qualification = form.qualification.data
            teacher.experience = form.experience.data
            teacher.joining_date = form.joining_date.data
            teacher.address = form.address.data
            teacher.salary = form.salary.data
            new_class_id = form.managed_class_id.data
            
            old_class = Class.query.filter_by(class_teacher_id=teacher.id).first()
            if old_class:
                old_class.class_teacher_id = None

            if new_class_id:
                new_class = Class.query.get(new_class_id)

                if new_class:
                    new_class.class_teacher_id =teacher.id

           
            db.session.commit()

            flash("Teacher updated successfully.", "success")

            return redirect(url_for("school_admin.manage_teachers"))

    return render_template(
    "school_admin/edit_teacher.html",
    form=form,
    teacher=teacher
    )

# Delete Route
@school_admin.route("/teacher/<int:id>/delete", methods=["POST"])
@login_required
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    # Get the related User account
    user = teacher.user
    # Remove teacher from managed class
    managed_class = Class.query.filter_by(
    class_teacher_id=teacher.id
    ).first()
    if managed_class:
        managed_class.class_teacher_id = None
    # Delete Teacher
    db.session.delete(teacher)
    # Delete User/login account
    if user:
        db.session.delete(user)
    db.session.commit()
    flash("Teacher and login account deleted successfully.", "success")
    return redirect(url_for("school_admin.manage_teachers"))
# For Teacher Subject Management System

@school_admin.route("/manage-teacher-subjects")
@login_required
def manage_teacher_subjects():

    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "").strip()

    query = TeacherSubject.query.filter_by(school_id=current_user.school_id)
    # Search by teacher name
    if search:
        query = query.join(Teacher).filter(or_(Teacher.first_name.ilike(f"%{search}%"),Teacher.last_name.ilike(f"%{search}%")
        )
        )

    teacher_subjects = query.order_by(TeacherSubject.created_at.desc()).paginate(page=page,per_page=10,error_out=False)
    return render_template("school_admin/manage_teacher_subjects.html",teacher_subjects=teacher_subjects,
    search=search)

# Create Subject Teacher

@school_admin.route("/create-teacher-subject", methods=["GET", "POST"])
@login_required
def create_teacher_subject():

    form = TeacherSubjectForm()

    # -----------------------------
    # Populate Teacher Dropdown
    # -----------------------------
    form.teacher_id.choices = [(t.id, f"{t.first_name} {t.last_name}")
    for t in Teacher.query.filter_by(school_id=current_user.school_id
    ).order_by(Teacher.first_name).all()]
    # -----------------------------
    # Populate Class Dropdown
    # -----------------------------
    form.class_id.choices = [(c.id, c.class_name)for c in Class.query.filter_by(
    school_id=current_user.school_id,is_active=True).order_by(Class.class_name).all()]
    # -----------------------------
    # Populate Section Dropdown
    # -----------------------------
    form.section_id.choices = [
    (s.id, s.section_name)for s in Section.query.filter_by(school_id=current_user.school_id
    ).order_by(Section.section_name).all()]
    # -----------------------------
    # Populate Subject Dropdown
    # -----------------------------
    form.subject_id.choices = [
    (s.id, s.subject_name)
    for s in Subject.query.filter_by(
    school_id=current_user.school_id
    ).order_by(Subject.subject_name).all()
    ]

    # -----------------------------
    # Save Assignment
    # -----------------------------
    if form.validate_on_submit():

        # Prevent duplicate assignment
        existing = TeacherSubject.query.filter_by(
        school_id=current_user.school_id,
        teacher_id=form.teacher_id.data,
        class_id=form.class_id.data,
        section_id=form.section_id.data,
        subject_id=form.subject_id.data
        ).first()

        if existing:
            flash(
            "This teacher has already been assigned to this class, section and subject.",
            "warning"
            )

            return redirect(
            url_for("school_admin.create_teacher_subject")
            )

        teacher_subject = TeacherSubject(
        school_id=current_user.school_id,
        teacher_id=form.teacher_id.data,
        class_id=form.class_id.data,
        section_id=form.section_id.data,
        subject_id=form.subject_id.data,
        academic_year=form.academic_year.data,
        is_active=bool(form.is_active.data)
        )

        db.session.add(teacher_subject)
        db.session.commit()

        flash(
        "Teacher subject assigned successfully.",
        "success"
        )

        return redirect(
        url_for("school_admin.manage_teacher_subjects")
        )

    return render_template(
    "school_admin/create_teacher_subject.html",
    form=form
    )

 
# For Detail Teacher Subject 
@school_admin.route("/teacher-subject/<int:id>")
@login_required
def teacher_subject_detail(id):

    teacher_subject = TeacherSubject.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()

    return render_template(
    "school_admin/teacher_subject_detail.html",
    teacher_subject=teacher_subject
    )

# For Edit Teacher Subject 

@school_admin.route(
"/teacher-subject/<int:id>/edit",
methods=["GET", "POST"]
)
@login_required
def edit_teacher_subject(id):

    teacher_subject = TeacherSubject.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()

    form = TeacherSubjectForm(obj=teacher_subject)

    # Teacher Dropdown
    form.teacher_id.choices = [
    (t.id, f"{t.first_name} {t.last_name}")
    for t in Teacher.query.filter_by(
    school_id=current_user.school_id
    ).order_by(Teacher.first_name).all()
    ]

    # Class Dropdown
    form.class_id.choices = [
    (c.id, c.class_name)
    for c in Class.query.filter_by(
    school_id=current_user.school_id,
    is_active=True
    ).order_by(Class.class_name).all()
    ]

    # Section Dropdown
    form.section_id.choices = [
    (s.id, s.section_name)
    for s in Section.query.filter_by(
    school_id=current_user.school_id
    ).order_by(Section.section_name).all()
    ]

    # Subject Dropdown
    form.subject_id.choices = [
    (s.id, s.subject_name)
    for s in Subject.query.filter_by(
    school_id=current_user.school_id
    ).order_by(Subject.subject_name).all()
    ]

    if form.validate_on_submit():

        teacher_subject.teacher_id = form.teacher_id.data
        teacher_subject.class_id = form.class_id.data
        teacher_subject.section_id = form.section_id.data
        teacher_subject.subject_id = form.subject_id.data
        teacher_subject.academic_year = form.academic_year.data
        teacher_subject.is_active = bool(form.is_active.data)

        db.session.commit()

        flash(
        "Teacher Subject updated successfully.",
        "success"
        )

        return redirect(
        url_for("school_admin.manage_teacher_subjects")
        )

    return render_template(
    "school_admin/edit_teacher_subject.html",
    form=form,
    teacher_subject=teacher_subject
    )



# For Delete Teacher Subject 
@school_admin.route(
"/teacher-subject/<int:id>/delete",
methods=["POST"]
)
@login_required
def delete_teacher_subject(id):

    teacher_subject = TeacherSubject.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()

    db.session.delete(teacher_subject)
    db.session.commit()

    flash(
    "Teacher Subject deleted successfully.",
    "success"
    )

    return redirect(
    url_for("school_admin.manage_teacher_subjects")
    )



# -------------------------------------------
#   ------ Subject Management ----------------
# ---------------------------------------------

@school_admin.route("/manage-subjects")

@login_required

def manage_subjects():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "", type=str)
    query = Subject.query.filter_by(school_id=current_user.school_id)
    if search:
        query = query.filter( Subject.subject_name.ilike(f"%{search}%"))

    subjects = query.order_by(Subject.subject_name.asc()).paginate(
        page=page,
        per_page=10,
        error_out=False
    )
    return render_template( "school_admin/manage_subjects.html",subjects=subjects,
        search=search )

# For Creating Subject
@school_admin.route("/create-subject", methods=["GET", "POST"])

@login_required

def create_subject():

    form = SubjectForm()
    if form.validate_on_submit():

        # Check duplicate Subject Name

        existing_name = Subject.query.filter_by(
            school_id=current_user.school_id,
            subject_name=form.subject_name.data.strip()
        ).first()

        if existing_name:

            flash("A subject with this name already exists.","danger")
            return render_template("school_admin/create_subject.html",form=form)

        # Check duplicate Subject Code

        existing_code = Subject.query.filter_by( school_id=current_user.school_id,subject_code=form.subject_code.data.strip()
        ).first()

        if existing_code:

            flash("A subject with this code already exists.","danger" )
            return render_template( "school_admin/create_subject.html", form=form)
        # Create Subject
        subject = Subject(
            school_id=current_user.school_id,
            subject_name=form.subject_name.data.strip(),
            subject_code=form.subject_code.data.strip(),
            description=form.description.data.strip()
            if form.description.data else None,
            is_active=bool(form.is_active.data)
        )
        db.session.add(subject)
        db.session.commit()
        flash("Subject created successfully.","success")
        return redirect(url_for("school_admin.manage_subjects"))

    return render_template("school_admin/create_subject.html",form=form)



@school_admin.route("/subject/<int:id>")
@login_required
def subject_detail(id):
    subject = Subject.query.filter_by(id=id,school_id=current_user.school_id
    ).first_or_404()
    return render_template("school_admin/subject_detail.html",subject=subject )


@school_admin.route( "/subject/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_subject(id):
    subject = Subject.query.filter_by(id=id,school_id=current_user.school_id).first_or_404()
    form = SubjectForm(obj=subject)
    if form.validate_on_submit():
        # Check duplicate subject name
        existing_name = Subject.query.filter(Subject.id != subject.id,Subject.school_id == current_user.school_id,
            Subject.subject_name == form.subject_name.data.strip()).first()
        if existing_name:
            flash("Subject name already exists.","danger")
            return render_template("school_admin/edit_subject.html",form=form,subject=subject)
        # Check duplicate subject code
        existing_code = Subject.query.filter(
            Subject.id != subject.id,
            Subject.school_id == current_user.school_id,
            Subject.subject_code == form.subject_code.data.strip()
        ).first()
        if existing_code:
            flash("Subject code already exists.","danger")
            return render_template("school_admin/edit_subject.html",form=form,subject=subject)
        subject.subject_name = form.subject_name.data.strip()
        subject.subject_code = form.subject_code.data.strip()
        subject.description = (
            form.description.data.strip()
            if form.description.data
            else None
        )
        subject.is_active = bool(form.is_active.data)
        db.session.commit()
        flash("Subject updated successfully.","success")
        return redirect(url_for("school_admin.manage_subjects"))

    return render_template("school_admin/edit_subject.html",form=form,subject=subject)




@school_admin.route("/subject/<int:id>/delete",methods=["POST"])
@login_required
def delete_subject(id):
    subject = Subject.query.filter_by(id=id,school_id=current_user.school_id
    ).first_or_404()
    db.session.delete(subject)
    db.session.commit()
    flash("Subject deleted successfully.","success")
    return redirect(url_for("school_admin.manage_subjects"))





# -------------------------------------------
#   ------ Student Management System ----------------
# ---------------------------------------------
 # For  Manage Section

@school_admin.route("/create-student", methods=["GET", "POST"])
@login_required
def create_student():

    form = StudentForm()

    # Get current school
    school_id = current_user.school_id

    # -----------------------------
    # Populate Class dropdown
    # -----------------------------
    classes = Class.query.filter_by(
    school_id=school_id,
    is_active=True
    ).all()

    form.class_id.choices = [
    (c.id, c.class_name)
    for c in classes
    ]

    # -----------------------------
    # Populate Section dropdown
    # -----------------------------
    sections = Section.query.filter_by(
    school_id=school_id
    ).all()

    form.section_id.choices = [
    (s.id, s.section_name)
    for s in sections
    ]

    # -----------------------------
    # POST
    # -----------------------------
    if form.validate_on_submit():

        try:

            # =====================================
            # 1. Check if email already exists
            # =====================================

            existing_user = User.query.filter_by(
            email=form.email.data
            ).first()

            if existing_user:
                flash("A user with this email already exists.", "danger")
                return render_template(
                "school_admin.create_student.html",
                form=form
                )

            # =====================================
            # 2. Get Student Role
            # =====================================

            student_role = Role.query.filter_by(
            role_name="Student"
            ).first()

            if not student_role:
                flash("Student role was not found.", "danger")
                return render_template(
                "school_admin.create_student.html",
                form=form
                )

            # =====================================
            # 3. Generate Student Password
            # =====================================

            generated_password = form.admission_number.data

            # =====================================
            # 4. Create User
            # =====================================

            user = User(
            full_name=f"{form.first_name.data} {form.last_name.data}",

            username=form.email.data,

            email=form.email.data,

            role_id=student_role.id,

            school_id=school_id,

            is_active=True,

            is_verified=False
            )

            # Hash password
            user.password_hash = bcrypt.generate_password_hash(
            generated_password
            ).decode("utf-8")

            db.session.add(user)

            # Get user.id
            db.session.flush()

            # =====================================
            # 5. Create Student
            # =====================================

            student = Student(

            # User relationship
            user_id=user.id,

            # School
            school_id=school_id,

            # Personal Information
            first_name=form.first_name.data,
            last_name=form.last_name.data,

            gender=form.gender.data,

            date_of_birth=form.date_of_birth.data,

            phone=form.phone.data,

            address=form.address.data,

            # Academic Information
            admission_number=form.admission_number.data,

            roll_number=form.roll_number.data,

            class_id=form.class_id.data,

            section_id=form.section_id.data,

            admission_date=form.admission_date.data,
            cnic = form.cnic.data,

            # Guardian
            guardian_name=form.guardian_name.data,

            guardian_phone=form.guardian_phone.data
            )

            db.session.add(student)

            # =====================================
            # 6. Commit Everything
            # =====================================

            db.session.commit()

            print("STUDENT CREATED SUCCESSFULLY!")

            # =====================================
            # 7. Show Credentials Page
            # =====================================

            return render_template(
            "school_admin/student_credentials.html",

            student=student,

            email=user.email,

            password=generated_password
            )

        except Exception as e:

            db.session.rollback()

            print("ERROR CREATING STUDENT:", e)

            flash(
            "An error occurred while creating the student.",
            "danger"
            )

            return render_template(
            "school_admin/create_student.html",
            form=form
            )

    return render_template(
    "school_admin/create_student.html",
    form=form
    )

@school_admin.route("/manage-students")
@login_required
def manage_students():

    students = Student.query.filter_by(
    school_id=current_user.school_id
    ).order_by(
    Student.id.desc()
    ).all()

    return render_template(
    "school_admin/manage_students.html",
    students=students
    )


@school_admin.route("/student/<int:id>")
@login_required
def student_detail(id):

    student = Student.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()
    print("CNIC: ", student.cnic)
    return render_template(
    "school_admin/student_detail.html",
    student=student
    )

@school_admin.route("/student/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_student(id):

    student = Student.query.filter_by(
    id=id,
    school_id=current_user.school_id
    ).first_or_404()

    form = StudentForm(obj=student)

    # --------------------------------------------------
    # Classes
    # --------------------------------------------------

    classes = Class.query.filter_by(
    school_id=current_user.school_id,
    is_active=True
    ).all()

    form.class_id.choices = [
    (0, "-- Select Class --")
    ] + [
    (c.id, c.class_name)
    for c in classes
    ]

    # --------------------------------------------------
    # Sections
    # --------------------------------------------------

    sections = Section.query.filter_by(
    school_id=current_user.school_id
    ).all()

    form.section_id.choices = [
    (0, "-- Select Section --")
    ] + [
    (s.id, s.section_name)
    for s in sections
    ]

    # --------------------------------------------------
    # Submit
    # --------------------------------------------------

    if form.validate_on_submit():

    # ----------------------------------------------
    # Check duplicate email
    # ----------------------------------------------

        existing_user = User.query.filter(
        User.email == form.email.data.strip().lower(),
        User.id != student.user_id
        ).first()

        if existing_user:

            flash(
            "This email is already being used by another user.",
            "danger"
            )

            return render_template(
            "school_admin/edit_student.html",
            form=form,
            student=student
            )

    # ----------------------------------------------
    # Check duplicate admission number
    # ----------------------------------------------

        existing_student = Student.query.filter(
        Student.admission_number ==
        form.admission_number.data.strip(),
        Student.id != student.id,
        Student.school_id ==current_user.school_id).first()
        if existing_student:
            flash(
            "This admission number already exists.",
            "danger"
            )
            return render_template(
            "school_admin/edit_student.html",
            form=form,
            student=student
            )

    # ----------------------------------------------
    # Update User
    # ----------------------------------------------

        user = student.user

        email = form.email.data.strip().lower()

        user.email = email
        user.username = email

        # ----------------------------------------------
        # Update Student
        # ----------------------------------------------

        student.first_name = form.first_name.data.strip()
        student.last_name = form.last_name.data.strip()

        student.email = email

        student.phone = (
        form.phone.data.strip()
        if form.phone.data
        else None
        )

        student.gender = form.gender.data

        student.date_of_birth = form.date_of_birth.data

        student.cnic = (
        form.cnic.data.strip()
        if form.cnic.data
        else None
        )

        student.admission_number = (
        form.admission_number.data.strip()
        )

        student.roll_number = (
        form.roll_number.data.strip()
        if form.roll_number.data
        else None
        )
        if request.method=="GET":
            student.class_id = form.class_id.data
            student.section_id = form.section_id.data
        student.admission_date = form.admission_date.data
        student.guardian_name = (
        form.guardian_name.data.strip()
        if form.guardian_name.data
        else None
        )

        student.guardian_phone = (
        form.guardian_phone.data.strip()
        if form.guardian_phone.data
        else None
        )

        student.address = (
        form.address.data.strip()
        if form.address.data
        else None
        )

        # ----------------------------------------------
        # Save
        # ----------------------------------------------

        try:

            db.session.commit()
            flash("Student updated successfully.","success")
            return redirect(url_for("school_admin.student_detail",id=student.id))
        except Exception as e:
            db.session.rollback()
            print("ERROR UPDATING STUDENT:", e)
            flash("An error occurred while updating the student.","danger")

    return render_template("school_admin/edit_student.html",form=form,student=student)






@school_admin.route("/student/<int:id>/delete", methods=["POST"])
@login_required
def delete_student(id):

        student = Student.query.filter_by(
        id=id,
        school_id=current_user.school_id
        ).first_or_404()

        try:

            db.session.delete(student)

            db.session.commit()

            flash(
            "Student deleted successfully.",
            "success"
            )

        except Exception as e:

            db.session.rollback()

            print("ERROR DELETING STUDENT:", e)

            flash(
            "Unable to delete student.",
            "danger"
            )

        return redirect(
        url_for("school_admin.manage_students")
        )
