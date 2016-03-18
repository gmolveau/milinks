from .app import app, manager, db, login_manager, material

@manager.command
def syncdb():
    '''Creates all missing tables.'''
    db.create_all()
