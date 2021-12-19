import datetime as dt
from flask import render_template, flash, url_for, redirect
from flask import request
from flask_login import login_required, logout_user, login_user
from . import auth
from ..models import User
from .forms import LoginForm


# Inject variable into all Jinja templates for `auth` blueprint
@auth.context_processor
def inject_now():
    return {'now': dt.datetime.utcnow()}


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            flash('Successfully signed in.')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
    return "ON SIGNUP PAGE"
