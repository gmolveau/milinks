# manage.py

from project import manager
import project.config

@manager.command
def syncdb():
    '''Creates all missing tables.'''
    db.create_all()

if __name__ == '__main__':
    manager.run()
