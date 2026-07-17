from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.user import User

app = create_app()

with app.app_context():



# ==========================
# Create Default Roles
# ==========================
    roles = [("Software Admin", "System Owner"),("School Admin", "School Administrator"),
    ("Teacher", "Teacher"),("Student", "Student"),("Parent", "Parent")]
    print("Current Roles:")
    for role_name, description in roles:
        role = Role.query.filter_by(role_name=role_name).first()

        if not role:
            role = Role(role_name=role_name,description=description)
            db.session.add(role)

    db.session.commit()

    print("✅ Roles created successfully.")

# ==========================
# Create Software Admin
# ==========================
    admin = User.query.filter_by(email="admin@eschool.com").first()

    if not admin:

        software_admin_role = Role.query.filter_by(role_name="Software Admin").first()

        admin = User(username="admin",email="admin@eschool.com",role_id=software_admin_role.id,school_id=None,is_active=True,is_verified=True)

        admin.set_password("Admin@123")

        db.session.add(admin)
        db.session.commit()

        print("✅ Software Admin created successfully.")

    else:
        print("ℹ️ Software Admin already exists.")

    print("✅ Database seeded successfully.")