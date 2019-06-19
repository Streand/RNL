from flask import Blueprint, jsonify
from Controller.drinkController import getDrink, createDrink
from Controller.foodController import getFood, createFood
from __init__ import app


routes_blueprint = Blueprint('routes', __name__)

# this is food
@routes_blueprint.route('/food', methods=['GET'])
def showAllFoods():
    return getFood()

@routes_blueprint.route('/food', methods=['POST'])
def createOneFood():
    return createFood()

# this is drink
@routes_blueprint.route('/drink', methods=['GET'])
def showAllDrinks():
    return getDrink()

@routes_blueprint.route('/drink', methods=['POST'])
def createOneDrink():
    return createDrink()
