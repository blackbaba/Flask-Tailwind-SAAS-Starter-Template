from flask import Blueprint

main = Blueprint('main', __name__)

# Import at bottom to avoid circular references
from . import views, errors
