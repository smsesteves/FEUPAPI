from bs4 import BeautifulSoup
from urllib.request import urlopen

EMENTAS_URL = "https://sigarra.up.pt/feup/pt/cantina.ementashow"
CAFETARIA_TABLE_ID = 2
RESTAURANTE_TABLE_ID = 3


def get_menu_cafetaria():
    try:
        content = urlopen(EMENTAS_URL)
        html = content.read()
    except Exception:
        raise ConnectionError

    soup = BeautifulSoup(html, "lxml")
    soup = soup.find_all("table", "dados")[CAFETARIA_TABLE_ID]
    soup = soup.find_all("tr")
    soup = soup[1:]

    table_data = []

    for row in soup:
        row_data = row.find_all("td", "d")
        table_data.append([value.string for value in row_data])

    return table_data


def get_menu_restaurante():
    try:
        content = urlopen(EMENTAS_URL)
        html = content.read()
    except Exception:
        raise ConnectionError

    soup = BeautifulSoup(html, "lxml")
    soup = soup.find_all("table", "dados")[RESTAURANTE_TABLE_ID]
    soup = soup.find_all("tr")
    soup = soup[1:]

    table_data = []

    for row in soup:
        row_data = row.find_all("td", "d")
        table_data.append([value.string for value in row_data])

    return table_data
