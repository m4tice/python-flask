from flask import render_template, jsonify
from app import app
from app.models import DataDB

data_db = DataDB()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    data = data_db.get_data()
    return jsonify(data)

@app.route('/add_random_data')
def add_random_data():
    data_db.add_random_data()
    return 'Data added'
