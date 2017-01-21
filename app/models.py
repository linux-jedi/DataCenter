from app import db

class Crashes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    plane_type = db.Column(db.String(100))
    aboard = db.Column(db.Integer)
    fatalities = db.Column(db.Integer)
    summary = db.Column(db.Text)