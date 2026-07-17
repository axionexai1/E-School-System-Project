from flask import Blueprint

software_admin= Blueprint("software_admin", __name__, url_prefix="/software-admin")

from . import routes