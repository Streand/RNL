
from __init__ import app, db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(50))