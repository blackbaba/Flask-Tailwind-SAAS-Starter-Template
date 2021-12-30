from flask import Blueprint
from ..models import Permission


main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


# Import at bottom to avoid circular references
from . import views, errors
