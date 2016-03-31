# from config import db
from flask import Blueprint, render_template, request, redirect

app_browse = Blueprint('browse', __name__)

@app_browse.route('/browse')
def browse():
	return render_template('browse.html')