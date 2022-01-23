from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post, Comment


def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(
            email=fake.email(),
            username=fake.user_name(),
            password='password',
            confirmed=True,
            name=fake.name(),
            location=fake.city(),
            about_me=fake.text(),
            member_since=fake.past_date()
        )
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def posts(count=100):
    fake = Faker()
    user_count = User.query.count()

    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(
            body=fake.text(),
            timestamp=fake.past_date(),
            author=u
        )
        db.session.add(p)
    db.session.commit()


def comments(count=10000):
    fake = Faker()
    post_count = Post.query.count()
    user_count = User.query.count()
    for i in range(count):
        p = Post.query.offset(randint(0, post_count - 1)).first()
        u = User.query.offset(randint(0, user_count - 1)).first()
        c = Comment(
            body=fake.text(),
            timestamp=fake.past_date(),
            author=u,
            post=p
        )
        db.session.add(c)
    db.session.commit()
