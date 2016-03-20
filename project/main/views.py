# project/main/views.py


#################
#### imports ####
#################

from flask import render_template
from flask.ext.login import login_required
from project import app


################
#### routes ####
################

@app.route('/')
@login_required
def home():
    return render_template('main/index.html')
