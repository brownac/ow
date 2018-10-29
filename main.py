import requests
from flask import Flask
from flask_cors import CORS, cross_origin
import json

from parser import scrape_page

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def prepare_data():
    URL = "https://masteroverwatch.com/leaderboards/pc/global/mode/ranked/category/skillrating/hero/overall/role/overall/data"
#    offsets = ["50"]
    entries = []
    offsets = []
    for i in range(1, 6):
        offsets.append(i * 50)
    for i in offsets:
        r = requests.get(url = URL, params = {'offset': i})
        data = r.json()
        entries.append(data['entries'])
    return entries

@app.route("/api")
@cross_origin()
def main():
    entries = prepare_data()
    names = scrape_page(entries)
    return json.dumps({'names': names})
