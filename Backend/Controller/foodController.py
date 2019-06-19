import sys
sys.path.append('..')

from Model.Food import Food
from __init__ import db
from flask import jsonify, request


def getFood():

    foods = Food.query.all()
     
    output = []

    for food in foods:
        food_data = {}
        food_data['id'] = food.id
        food_data['name'] = food.food
        output.append(food_data)

    return jsonify(output)


def createFood():

    data = request.get_json()

    new_food = Food(food=data['name'])
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message' : 'New food added!'})