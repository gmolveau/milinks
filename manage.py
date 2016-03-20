# manage.py

from project import app, db, manager

@manager.command
def create_db():
    '''Creates the db tables.'''
    db.create_all()

@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

if __name__ == '__main__':
    manager.run()
