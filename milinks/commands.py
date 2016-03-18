from .app import app, manager, db

@manager.command
def syncdb():
    '''Creates all missing tables.'''
    db.create_all()
