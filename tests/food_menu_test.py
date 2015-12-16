import unittest
import time
from src import consts
import src.food_menu as food_menu

# Minimum and maximum menus 'allowed' to be found on the website
MIN_MENUS = 1
MAX_MENUS = 10

# Failed connection string
CONNECTION_FAILED = "Connection failed!"


# Tests for the food menu api
class FoodMenuTest(unittest.TestCase):

    # Tests to see if the returned list has between 1 and 10 entries since the website shows atmost 2 weeks of menus.
    def test_cafeteria_length(self):
        test_list_cafeteria = food_menu.get_menu_cafeteria()
        self.assertGreaterEqual(len(test_list_cafeteria), MIN_MENUS)
        self.assertLessEqual(len(test_list_cafeteria), MAX_MENUS)

    # Tests to see if the date of the food menus are the present one or in the future. There are not past menus listed.
    def test_cafeteria_date(self):
        test_list_cafeteria = food_menu.get_menu_cafeteria()
        for menu in test_list_cafeteria:
            self.assertGreaterEqual(menu[consts.CAFETERIA_DATE], time.strftime(consts.CAFETERIA_DATE_FORMAT))

    # Tests to see if a connection could be established to the website.
    def test_cafeteria_valid_input(self):
        try:
            food_menu.get_menu_cafeteria()
        except ConnectionError:
            self.fail(CONNECTION_FAILED)

    # Tests to see if the cafeteria has returned all the info usually provided.
    def test_cafeteria_correct_values(self):
        test_list_cafeteria = food_menu.get_menu_cafeteria()
        for menu in test_list_cafeteria:
            self.assertEqual(len(menu), consts.CAFETERIA_DATA_SIZE)

    # Tests to see if the returned list has between 1 and 10 entries since the website shows atmost 2 weeks of menus.
    def test_restaurant_length(self):
        test_list_restaurant = food_menu.get_menu_restaurant()
        self.assertGreaterEqual(len(test_list_restaurant), 1)
        self.assertLessEqual(len(test_list_restaurant), 10)

    # Tests to see if the date of the food menus are the present one or in the future. There are not past menus listed.
    def test_restaurant_date(self):
        test_list_restaurant = food_menu.get_menu_restaurant()
        for menu in test_list_restaurant:
            self.assertGreaterEqual(menu[consts.RESTAURANT_DATE], time.strftime(consts.RESTAURANT_DATE_FORMAT))

    # Tests to see if a connection could be established to the website.
    def test_restaurant_valid_input(self):
        try:
            food_menu.get_menu_restaurant()
        except ConnectionError:
            self.fail(CONNECTION_FAILED)

    # Tests to see if the cafeteria has returned all the info usually provided.
    def test_restaurant_correct_values(self):
        test_list_restaurant = food_menu.get_menu_restaurant()
        for menu in test_list_restaurant:
            self.assertEqual(len(menu), consts.RESTAURANT_DATA_SIZE)
