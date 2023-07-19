# backend/api/__init__.py

from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import views to register route
import views
