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

import requests

def getJsonData():
    response = requests.get("http://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def pushToFirebase(a_json):
    credence = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin.initialize_app(credence, {
        'databaseURL' : 'https://sampledatabase-2c030.firebaseio.com/'
    })
    PEOPLE_DB = db.reference('user_data')
    for dict in a_json:
        PEOPLE_DB.push({
            'email': dict['email'],
            'id': dict['id'],
            'name': dict['name']
        })


def main():
    listData = []
    listData = getJsonData()
    pushToFirebase(listData)

main()