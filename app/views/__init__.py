from flask import Blueprint

views_bp = Blueprint("main", __name__)
from app.views import routes
