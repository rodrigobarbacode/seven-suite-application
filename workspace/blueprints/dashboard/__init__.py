# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes