from app import db

class Crashes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    plane_type = db.Column(db.String(100))
    aboard = db.Column(db.Integer)
    fatalities = db.Column(db.Integer)
    summary = db.Column(db.Text)

class DroneStrikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strike_id = db.Column(db.String(10), unique=True, index=True)
    date = db.Column(db.DateTime)
    tribal_agency = db.Column(db.String(20))
    location = db.Column(db.String(35))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    total_killed = db.Column(db.Integer)
    civilians_killed = db.Column(db.Integer)