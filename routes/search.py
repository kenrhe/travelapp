from flask import Blueprint, render_template, request, redirect
from config import db

app_search = Blueprint('search', __name__)

@app_search.route('/search', methods=['GET', 'POST'])
def search():
    item = {}

    if request.method == 'POST':
        form = request.form
        city = db.cities.find_one({"city" : form['text'].lower().strip() })
        item['city'] = city

        return render_template('city.html', **item)

    return render_template('search.html', **item)