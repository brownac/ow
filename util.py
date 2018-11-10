import requests

def prepare_data():
    URL = "https://masteroverwatch.com/leaderboards/pc/global/mode/ranked/category/skillrating/hero/overall/role/overall/data"
    return [requests.get(url = URL, params = {'offset': i}).json()['entries'] for i in [j * 50 for j in range(6)]]