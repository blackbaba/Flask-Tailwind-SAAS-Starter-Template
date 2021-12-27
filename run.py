import os
from app import create_app, db
from app.models import Permission, User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)


# Shell Context Processor
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission)


# Run tests
@app.cli.command()
def test():
    """Run unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
