from flask import jsonify
import copy

from app import app
from models import Crashes, DroneStrikes, Meteorites

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
    jsonResponse = {"type": "FeatureCollection", "features": []}
    
    for crash in crashes:
        data = {}
        data["type"] = "Feature"
        data["properties"] = {}
        data["properties"]["name"] = "Crash: " + str(crash.fatalities) + " died"
        data["properties"]["popupContent"] = crash.summary

        data["geometry"] = {}
        data["geometry"]["type"] = "Point"
        data["geometry"]["coordinates"] = [crash.longitude, crash.latitude]

        jsonResponse['features'].append(copy.deepcopy(data))
    
    resp = jsonify(**jsonResponse)
    resp.status_code = 200
    return resp

@app.route('/strikes', methods=['GET'])
def get_all_strikes():
    strikes = DroneStrikes.query.order_by(DroneStrikes.id)

    jsonResponse = {"type": "FeatureCollection", "features": []}

    for strike in strikes:
        data = {}
        data["type"] = "Feature"
        data["properties"] = {}
        data["properties"]["name"] = strike.strike_id
        data["properties"]["popupContent"] = str(strike.civilians_killed) + " civilians killed out of " +\
            str(strike.total_killed) + " total people killed"

        data["geometry"] = {}
        data["geometry"]["type"] = "Point"
        data["geometry"]["coordinates"] = [strike.longitude, strike.latitude]

        jsonResponse['features'].append(copy.deepcopy(data))

    resp = jsonify(**jsonResponse)
    resp.status_code = 200
    return resp

@app.route('/meteorites', methods=['GET'])
def get_meteorites():
    meteorites = Meteorites.query.order_by(Meteorites.id)

    jsonResponse = {"type": "FeatureCollection", "features": []}
    
    for meteor in meteorites:
        data = {}
        data["type"] = "Feature"
        data["properties"] = {}
        data["properties"]["name"] = meteor.name
        data["properties"]["popupContent"] = "Year: " + str(meteor.year) + " Mass: " + str(meteor.mass)

        data["geometry"] = {}
        data["geometry"]["type"] = "Point"
        data["geometry"]["coordinates"] = [meteor.longitude, meteor.latitude]

        jsonResponse['features'].append(copy.deepcopy(data))

    resp = jsonify(**jsonResponse)
    resp.status_code = 200
    return resp