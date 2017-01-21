from flask import jsonify
import copy

from app import app
from models import Crashes

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/dataset', methods=['GET'])
def get_dataset():
    return 0

@app.route('/crashes', methods=['GET'])
def get_crashes():
    crashes = Crashes.query.order_by(Crashes.id)
    jsonResponse = {"crashes":[]}
    
    for crash in crashes:
        data = {}
        data["type"] = "Feature"
        data["properties"] = {}
        data["properties"]["name"] = "Crash: " + str(crash.fatalities) + " died"
        data["properties"]["popupContent"] = crash.summary

        data["geometry"] = {}
        data["geometry"]["type"] = "Point"
        data["geometry"]["coordinates"] = [crash.latitude, crash.longitude]

        jsonResponse['crashes'].append(copy.deepcopy(data))
    
    resp = jsonify(**jsonResponse)
    resp.status_code = 200
    return resp



