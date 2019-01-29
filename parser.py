from bs4 import BeautifulSoup

def get_skill_rating(row):
    return row.find("div", class_="table-main-value").strong.text.strip()

def get_name(row):
    return row.find("span", class_="table-name-block").strong.text.strip()

def get_tag(row):
    return row.find("a", class_="table-row-link").get("href").split('-')[1]

def get_player_info(entries):
    players = []
    for entry in entries:
        for document in entry:
            soup = BeautifulSoup(document, 'html.parser')
            for row in soup.find_all("div", class_="table-row"):
                attributes = {}
                name = get_name(row)
                tag = get_tag(row)
                skill_rating = get_skill_rating(row)
                attributes["name"] = name
                attributes["tag"] = tag
                attributes["skill_rating"] = skill_rating
                players.append(attributes)
    return players

def get_individual_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    print soup.prettify(html)