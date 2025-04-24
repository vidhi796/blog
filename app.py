from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dash.html')

@app.route('/sales-growth.json')
def get_sales_growth():
    with open('sales-growth.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)
