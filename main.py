import requests
from flask import Flask
from flask_cors import CORS, cross_origin
import json

from parser import get_player_info

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def prepare_data():
    URL = "https://masteroverwatch.com/leaderboards/pc/global/mode/ranked/category/skillrating/hero/overall/role/overall/data"
    return [requests.get(url = URL, params = {'offset': i}).json()['entries'] for i in [j * 50 for j in range(6)]]

@app.route("/api")
@cross_origin()
def main():
    entries = prepare_data()
    players = get_player_info(entries)
    return json.dumps({'players': players})
