from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

try:
    from app import app, db
    from wanikanireverse import fetch_cards
except ModuleNotFoundError:
    from .app import app, db
    from .wanikanireverse import fetch_cards

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def fetch():
    print('Fetch!')
    fetch_cards()
    print('Cards pulled, bark bark')

if __name__ == '__main__':
    manager.run()
