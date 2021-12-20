import datetime as dt
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..email import send_email, send_async_email


# Inject variable into all Jinja templates for `main` blueprint
@main.context_processor
def inject_now():
    return {'now': dt.datetime.utcnow()}


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


@main.route('/health')
def health_check():
    return render_template('health.html')
