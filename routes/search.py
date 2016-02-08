from flask import Blueprint, render_template, request, redirect

app_search = Blueprint('search', __name__)

@app_search.route('/search')
def search():
	return render_template('search.html')