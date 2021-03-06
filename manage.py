from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Security_update,Comment

# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    Test function to run the unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Security_update = Security_update, Comment = Comment)

if __name__ == '__main__':
    manager.run()