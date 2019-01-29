import requests
from string import Template

def prepare_data():
    URL = "https://masteroverwatch.com/leaderboards/pc/global/mode/ranked/category/skillrating/hero/overall/role/overall/data"
    return [requests.get(url = URL, params = {'offset': i}).json()['entries'] for i in [j * 50 for j in range(6)]]

def fetch_player_by_tag(tag):
    URL = Template("https://masteroverwatch.com/profile/pc/global/${player_tag}").substitute(player_tag=tag)
    r = requests.get(url=URL)
    text = r.text
    return text.decode('utf-8').decode()