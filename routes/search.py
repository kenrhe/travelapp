from flask import Blueprint, render_template, request, redirect
from config import db

app_search = Blueprint('search', __name__)

@app_search.route('/search')
def search():
    return db.cities.find()
    return render_template('search.html')