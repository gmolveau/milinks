# project/__init__.py

#################
#### imports ####
#################

from .app import app, manager, db, login_manager, material
from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_material import Material
from flask_collect import Collect
import project.config


################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = _secret_key
# use uuidgen to generate the secret key


app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql://'+db_user+':'+db_pass+'@'+db_base+'/db?charset=utf8'
)

####################
#### extensions ####
####################


login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

mail = Mail(app)

toolbar = DebugToolbarExtension(app)

manager = Manager(app)

login_manager = LoginManager(app)

material = Material(app)

collect = Collect()
collect.init_app(app)
collect.init_script(manager)

db = SQLAlchemy(app)

########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500