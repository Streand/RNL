from flask import Blueprint, jsonify
from Controller.drinkController import getDrink, createDrink, updateDrink, deleteDrink
from Controller.foodController import getFood, createFood, updateFood, deleteFood
from __init__ import app


routes_blueprint = Blueprint('routes', __name__)

# this is food
@routes_blueprint.route('/food', methods=['GET'])
def showAllFoods():
    return getFood()

@routes_blueprint.route('/food', methods=['POST'])
def createOneFood():
    return createFood()

@routes_blueprint.route('/food/<id>', methods=['PUT'])
def updateOneFood(id):
    return updateFood(id)

@routes_blueprint.route('/food/<id>', methods=['DELETE'])
def deleteOneFood(id):
    return deleteFood(id)

# this is drink
@routes_blueprint.route('/drink', methods=['GET'])
def showAllDrinks():
    return getDrink()

@routes_blueprint.route('/drink', methods=['POST'])
def createOneDrink():
    return createDrink()

@routes_blueprint.route('/drink/<id>', methods=['PUT'])
def updateOneDrink(id):
    return updateDrink(id)

@routes_blueprint.route('/drink/<id>', methods=['DELETE'])
def deleteOneDrink(id):
    return deleteDrink(id)
