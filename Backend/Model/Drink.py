from __init__ import app, db

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink = db.Column(db.String(50))