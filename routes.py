from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from parser import get_player_info
from util import prepare_data
from db import insert_user, login
from auth import verify_token

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_envvar('APP_SETTINGS')

@app.route("/players")
@cross_origin()
def player_list():
    entries = prepare_data()
    players = get_player_info(entries)
    return json.dumps({'players': players})

@app.route("/players/<tag>")
@cross_origin()
def get_player(tag):
    key = app.config['SECRET_KEY']
    token = request.headers['Authorization'].split('Bearer ')[1]
    decoded = verify_token(token, key)
    if 'iss' in decoded:
        return json.dumps({'key': 'value'})
    else:
        return "Not authorized!", 403

@app.route("/users/create", methods=['POST'])
@cross_origin()
def create_user():
    if request.method == 'POST':
        key = app.config['SECRET_KEY']
        dataDict = json.loads(request.data)
        username = dataDict['username']
        password = dataDict['password']
        return json.dumps(insert_user(username, password, key))

@app.route("/users/login", methods=['POST'])
@cross_origin()
def login_user():
    if request.method == 'POST':
        key = app.config['SECRET_KEY']
        dataDict = json.loads(request.data)
        username = dataDict['username']
        password = dataDict['password']
        return json.dumps(login(None, username, password, key))
