from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    profession = db.Column(db.String(50))
    goals = db.Column(db.Text)
    interests = db.Column(db.Text)
    time_frame = db.Column(db.String(20))  
