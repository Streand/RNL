import sys
sys.path.append('..')

from Model.Drink import Drinks
from __init__ import db
from flask import jsonify, request

def getDrink():

    drinks = Drinks.query.all()
     
    output = []

    for drink in drinks:
        drink_data = {}
        drink_data['id'] = drink.id
        drink_data['name'] = drink.drink
        output.append(drink_data)

    return jsonify(output)


def createDrink():

    data = request.get_json()

    new_drink = Drinks(drink=data['name'])
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({'message' : 'New drink added!'})


def updateDrink(id):

    data = request.get_json()

    new_drink = Drinks(drink=data['name'])

    drink = Drinks.query.filter_by(id=id).first()

    drink.drink = new_drink.drink
    db.session.commit()
    return jsonify({'message' : 'updated!'})

def deleteDrink(id):

    drink = Drinks.query.filter_by(id=id).first()
    db.session.delete(drink)
    db.session.commit()
    return jsonify ({'message' : 'drink deleted!'})