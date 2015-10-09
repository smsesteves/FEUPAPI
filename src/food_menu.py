from bs4 import BeautifulSoup
from urllib.request import urlopen

# URL that contains information about the food menus of FEUP
MENUS_URL = "https://sigarra.up.pt/feup/pt/cantina.ementashow"
# [HARDCODED] From the tables containing the information, the cafeteria is the third and the restaurant is the forth
#             hence the ids to be used on the array of data retreived are 2 and 3 respectively
CAFETERIA_TABLE_ID = 2
RESTAURANT_TABLE_ID = 3


# Gets the food menu information for the cafeteria
# Returns: Data in a list where each element is a list with the following format:
# [Day of the Week, Date(dd-mm-yyyy), Meat dish, Fish dish, Vegetarian dish, Diet dish]
def get_menu_cafeteria():
    # Tries to open the MENNUS_URL. Raises a ConnectionError if it is unable to connect.
    try:
        content = urlopen(MENUS_URL)
        html = content.read()
    except Exception:
        raise ConnectionError

    # Loads the HTML aand finds the relevant tables.
    soup = BeautifulSoup(html, "lxml")
    soup = soup.find_all("table", "dados")[CAFETERIA_TABLE_ID]  # [HAARDCODED] See above for a description
    soup = soup.find_all("tr")
    soup = soup[1:]  # Removes the first row of results since they are the names of the fields in each column

    # Creates the list we will be returning
    table_data = []

    # Fills the list with a list with the values from each row. See get_menu_cafeteria note for additional info.
    for row in soup:
        row_data = row.find_all("td", "d")
        table_data.append([value.string for value in row_data])

    return table_data


# Gets the food menu information for the restaurant
# Returns: Data in a list where each element is a list with the following format:
# [Day of the Week, Date(dd-mm-yyyy), Meat dish, Fish dish]
def get_menu_restaurant():
    # Tries to open the MENNUS_URL. Raises a ConnectionError if it is unable to connect.
    try:
        content = urlopen(MENUS_URL)
        html = content.read()
    except Exception:
        raise ConnectionError

    # Loads the HTML aand finds the relevant tables.
    soup = BeautifulSoup(html, "lxml")
    soup = soup.find_all("table", "dados")[RESTAURANT_TABLE_ID]  # [HAARDCODED] See above for a description
    soup = soup.find_all("tr")
    soup = soup[1:]  # Removes the first row of results since they are the names of the fields in each column

    # Creates the list we will be returning
    table_data = []

    # Fills the list with a list with the values from each row. See get_menu_cafeteria note for additional info.
    for row in soup:
        row_data = row.find_all("td", "d")
        table_data.append([value.string for value in row_data])

    return table_data
