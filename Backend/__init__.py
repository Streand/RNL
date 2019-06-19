from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Eirik/Documents/MyProjects/RNL/Backend/randomizer.db'

db = SQLAlchemy(app)
