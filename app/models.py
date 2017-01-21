from app import db

class DataSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

class AirplaneCrashes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    plane_type = db.Column(db.String(100))
    aboard = db.Column(db.Integer)
    fatalities = db.Column(db.Integer)
    summary = db.Column(db.Text)