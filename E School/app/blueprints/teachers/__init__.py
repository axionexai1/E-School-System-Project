from flask import Blueprint

teachers = Blueprint(
"teachers",
__name__,
url_prefix="/teacher"
)

from . import routes