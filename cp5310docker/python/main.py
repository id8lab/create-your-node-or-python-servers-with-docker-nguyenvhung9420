import pymongo
from bson.json_util import dumps
import json
from bson.objectid import ObjectId

from flask import Response
from flask import request
from flask import Flask
from flask import jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

#GET ALL PEOPLE IN THE DATABASE:
@app.route('/allpeople', methods = ['GET'])
def readAllPeople():
    allPeople = PEOPLE_DB.get()
    if not allPeople:
        return 'Resource not found', 404
    return jsonify(allPeople)

#GET PERSON/PEOPLE BY ID
@app.route('/person', methods = ['GET'])
def readPerson():
    person_id = int(request.args['id'])
    aPerson = PEOPLE_DB.order_by_child("id").equal_to(person_id).get()
    if not aPerson:
        return 'Resource not found', 404
    return jsonify(aPerson)

#MAIN
if __name__ == '__main__':
    credence = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin.initialize_app(credence, {
        'databaseURL' : 'https://sampledatabase-2c030.firebaseio.com/'
    })
    PEOPLE_DB = db.reference('user_data')
    app.run()