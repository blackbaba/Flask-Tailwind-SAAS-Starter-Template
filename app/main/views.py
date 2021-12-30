import datetime as dt
from flask import render_template, session, redirect, url_for, flash
from flask_login.utils import login_required
from . import main
from .forms import NameForm
from .. import db
from ..email import send_email, send_async_email
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
def index():
    # flash('This is an error !', category='error')
    # flash('This is an informational message.', category='information',)
    return render_template('index.html')


@main.route('/terms-and-conditions')
def terms_conditions():
    return "This is the terms and conditions page"


@main.route('/privacy')
def privacy():
    return "This is the privacy policy page"


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'Administrator Access'


@main.route('/health')
def health_check():
    return render_template('health.html')
