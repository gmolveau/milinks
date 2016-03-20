# project/__init__.py

#################
#### imports ####
#################

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask_mail import Mail
from flask_material import Material
from flask_collect import Collect
from flask.ext.debugtoolbar import DebugToolbarExtension
from .config import DevelopmentConfig, TestingConfig, ProductionConfig


################
#### config ####
################

app = Flask(__name__)

dev = DevelopmentConfig()
#prod = ProductionConfig
#test = TestingConfig
app.config.from_object( dev)


####################
#### extensions ####
####################

manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
toolbar = DebugToolbarExtension(app)
material = Material(app)
collect = Collect()
collect.init_app(app)
collect.init_script(manager)
db = SQLAlchemy(app)

####################
#### blueprints ####
####################

from project.main.views import main_blueprint
from project.user.views import user_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)

#####################
#### flask-login ####
#####################

from project.models import User

login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

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