from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_material import Material
from .credentials import db_user, db_pass, db_base

app = Flask(__name__)

manager = Manager(app)

login_manager = LoginManager(app)

material = Material(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = "efd04c67-1745-476e-a18a-6295999a2eca"
# use


app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql://'+db_user+':'+db_pass+'@'+db_base+'/db?charset=utf8'
)
db = SQLAlchemy(app)
