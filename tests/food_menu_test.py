import unittest
import time
import src.food_menu as food_menu

# Minimum and maximum menus 'allowed' to be found on the website
MIN_MENUS = 1
MAX_MENUS = 10

# Cafetria list structure: [Day of the Week, Date(dd-mm-yyyy), Meat dish, Fish dish, Vegetarian dish, Diet dish]
CAFETERIA_DATA_SIZE = 6
CAFETERIA_DOTW = 0
CAFETERIA_DATE = 1
CAFETERIA_MEAT = 2
CAFETERIA_FISH = 3
CAFETERIA_VEGE = 4
CAFETERIA_DIET = 5
CAFETERIA_DATE_FORMAT = "%d-%m-%Y"

# Restaurant list structure: [Day of the Week, Date(dd-mm-yyyy), Meat dish, Fish dish]
RESTAURANT_DATA_SIZE = 4
RESTAURANT_DOTW = 0
RESTAURANT_DATE = 1
RESTAURANT_MEAT = 2
RESTAURANT_FISH = 3
RESTAURANT_DATE_FORMAT = "%d-%m-%Y"

# Failed connection string
CONNECTION_FAILED = "Connection failed!"


# Tests for the food menu api
class FoodMenuTest(unittest.TestCase):

    # Tests to see if the returned list has between 1 and 10 entries since the website shows atmost 2 weeks of menus.
    def test_cafeteria_length(self):
        test_list_cafetaria = food_menu.get_menu_cafeteria()
        self.assertGreaterEqual(len(test_list_cafetaria), MIN_MENUS)
        self.assertLessEqual(len(test_list_cafetaria), MAX_MENUS)

    # Tests to see if the date of the food menus are the present one or in the future. There are not past menus listed.
    def test_cafetaria_date(self):
        test_list_cafetaria = food_menu.get_menu_cafeteria()
        for menu in test_list_cafetaria:
            self.assertGreaterEqual(menu[CAFETERIA_DATE], time.strftime(CAFETERIA_DATE_FORMAT))

    # Tests to see if a connection could be established to the website.
    def test_cafetaria_valid_input(self):
        try:
            food_menu.get_menu_cafeteria()
        except ConnectionError:
            self.fail(CONNECTION_FAILED)

    # Tests to see if the cafeteria has returned all the info usually provided.
    def test_cafetaria_correct_values(self):
        test_list_cafetaria = food_menu.get_menu_cafeteria()
        for menu in test_list_cafetaria:
            self.assertEqual(len(menu), CAFETERIA_DATA_SIZE)

    # Tests to see if the returned list has between 1 and 10 entries since the website shows atmost 2 weeks of menus.
    def test_retaurante_length(self):
        test_list_restaurante = food_menu.get_menu_restaurant()
        self.assertGreaterEqual(len(test_list_restaurante), 1)
        self.assertLessEqual(len(test_list_restaurante), 10)

    # Tests to see if the date of the food menus are the present one or in the future. There are not past menus listed.
    def test_restaurante_date(self):
        test_list_restaurante = food_menu.get_menu_restaurant()
        for menu in test_list_restaurante:
            self.assertGreaterEqual(menu[RESTAURANT_DATE], time.strftime(RESTAURANT_DATE_FORMAT))

    # Tests to see if a connection could be established to the website.
    def test_restaurante_valid_input(self):
        try:
            food_menu.get_menu_restaurant()
        except ConnectionError:
            self.fail(CONNECTION_FAILED)

    # Tests to see if the cafeteria has returned all the info usually provided.
    def test_restaurante_correct_values(self):
        test_list_restaurante = food_menu.get_menu_restaurant()
        for menu in test_list_restaurante:
            self.assertEqual(len(menu), RESTAURANT_DATA_SIZE)
