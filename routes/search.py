from flask import Blueprint, render_template, request, redirect
from config import db

from browse import city

app_search = Blueprint('search', __name__)

@app_search.route('/search', methods=['GET', 'POST'])
def search():
    item = {}

    if request.method == 'POST':
        form = request.form
        city_data = db.cities.find_one({"city" : form['text'].lower().strip().replace(" ", "-") })

        return redirect('/' + city_data['_id'])

    return render_template('search.html', **item)