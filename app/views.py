from flask import jsonify
import copy

from app import app
from models import AirplaneCrashes

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/dataset', methods=['GET'])
def get_dataset():
    return 0

@app.route('/crashes', methods=['GET'])
def get_crashes():
    crashes = AirplaneCrashes.query.order_by(AirplaneCrashes.id)
    jsonResponse = {"crashes":[]}
    
    for crash in crashes:
        data = {}
        data['id'] = crash.id
        data['longitude'] = crash.longitude
        data['latitude'] = crash.latitude
        data['plane_type'] = crash.plane_type
        data['aboard'] = crash.aboard
        data['fatalities'] = crash.fatalities
        data['summary'] = crash.summary
        jsonResponse['crashes'].append(copy.deepcopy(data))
    
    resp = jsonify(**jsonResponse)
    resp.status_code = 200
    return resp



