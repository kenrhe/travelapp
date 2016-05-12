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

        db.runCommand({ 'getParameter' : 1, 'textSearchEnabled' : 1})
        db.cities.ensure_index([('city', 'text'), ('state', 'text'), ('state_code', 'text')],name="default_index",weights={'city':100,'state':100, 'state_code' : 100})
        text_results = db.command('text', db.cities.name, search=form['text'],project={"_id": 1}, limit=100)

        print text_results

        return render_template('city.html', **item)

    return render_template('search.html', **item)