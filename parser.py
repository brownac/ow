from bs4 import BeautifulSoup

def scrape_page(entries):
    names = []
    for entry in entries:
        for document in entry:
            soup = BeautifulSoup(document, 'html.parser')
            for row in soup.find_all("span", class_="table-name-block"):
                names.append(row.strong.text.strip())
    return names    
        