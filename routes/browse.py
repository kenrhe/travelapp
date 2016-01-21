from config import db
from flask import Blueprint, render_template, request, redirect

app_browse = Blueprint('browse', __name__)

@app_locations.route('/browse')
def browse:
	locations = []

	for record in db.cities.find():
		ratings = record['ratings']
		total = 0.0
		counter = 0.0
 		
		for x in range(0, len(ratings)):
			total += float(str(ratings[x]))
			counter += 1.0

		average = total/counter
		hotels.append({ "_id" : str(record['_id']) , "name" : record['name'], "rating" : round(average, 2), "url" : str(record['_id']) })
	return render_template('browse.html', hotels=hotels)