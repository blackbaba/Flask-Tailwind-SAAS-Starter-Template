from email.mime import base
from email.policy import default
import os
import sys
import click
from app import create_app, db
from app.models import Permission, User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


# Shell Context Processor
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission)


# Run tests
@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Run tests under code coverage')
def test(coverage):
    """Run unit tests"""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print(f"HTML version: file://{covdir}/index.html")
        COV.erase()
