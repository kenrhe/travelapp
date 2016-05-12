# from config import db
from flask import Blueprint, render_template, request, redirect
from config import db

app_browse = Blueprint('browse', __name__)

@app_browse.route('/browse')
def browse():
	return render_template('browse.html')

@app_browse.route('/<country>/<state>/<city>')
def city(country, state, city):
	city = db.cities.find_one({"_id" : country + '/' + state + '/' + city })
	return render_template('city.html', city=city)