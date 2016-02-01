'''
Authored by: Kenneth Rhee, Joe Goodman
Email: kennethhrhee@gmail.com, goodman.a.joseph@gmail.com
'''

from routes.browse import app_browse
from flask import render_template, request
from config import app
import os
# from config import app, db

app.register_blueprint(app_browse)

#===================================
# Routes ####
#===================================
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)