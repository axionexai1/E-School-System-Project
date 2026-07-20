from flask import Blueprint

school_admin = Blueprint(
"school_admin",
__name__,
template_folder="templates"
)

from . import routes