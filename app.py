from routes.browse import app_browse
from flask import render_template, request

from config import app, db

application.register_blueprint(app_browse)

#===================================
# Routes ####
#===================================
@app.route('/')
def index():
	return render_template('index.html')