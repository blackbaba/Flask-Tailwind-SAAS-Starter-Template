import datetime as dt
from inspect import currentframe
import re
import timeago
from flask import render_template, session, redirect, url_for, flash, current_app, request
from flask_login.utils import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, PostForm
from .. import db
from ..models import Permission, Role, User, Post
from ..email import send_email, send_async_email
from ..decorators import admin_required


@main.context_processor
def inject_user():
    return dict(dt=dt, timeago=timeago, current_app=current_app)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items

    if form.validate_on_submit() and current_user.can(Permission.WRITE):
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully')
        return redirect(url_for('main.index'))
    # flash('This is an error !', category='error')
    # flash('This is an informational message.', category='information',)
    return render_template('index.html', form=form, posts=posts, pagination=pagination)


@main.route('/saas', methods=['GET', 'POST'])
def saas():
    return render_template('saas.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_last_seen_time_ago = timeago.format(
        user.last_seen, dt.datetime.utcnow())

    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('user.html', user=user, user_last_seen_time_ago=user_last_seen_time_ago, posts=posts, pagination=pagination)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('main.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<username>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.active = form.active.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('main.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.active.data = user.active
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile_admin.html', form=form)


@main.route('/terms-and-conditions')
def terms_conditions():
    return "Terms and conditions page"


@main.route('/privacy')
def privacy():
    return "Privacy policy page"


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'Administrator Access'


@main.route('/health')
def health_check():
    return render_template('health.html')
