import unittest
import time
import src.menu as menu_api


class MenuTest(unittest.TestCase):

    # TESTS FOR CAFETARIA
    def test_cafetaria_length(self):
        TEST_LIST_CAFETARIA = menu_api.get_menu_cafetaria()
        self.assertGreaterEqual(len(TEST_LIST_CAFETARIA), 1)
        self.assertLessEqual(len(TEST_LIST_CAFETARIA), 10)

    def test_cafetaria_date(self):
        TEST_LIST_CAFETARIA = menu_api.get_menu_cafetaria()
        for menu in TEST_LIST_CAFETARIA:
            self.assertGreaterEqual(menu[1], time.strftime("%d-%m-%Y"))

    def test_cafetaria_valid_input(self):
        try:
            menu_api.get_menu_cafetaria()
        except ConnectionError:
            self.fail("Connection failed!")

    def test_cafetaria_correct_values(self):
        TEST_LIST_CAFETARIA = menu_api.get_menu_cafetaria()
        for menu in TEST_LIST_CAFETARIA:
            self.assertEqual(len(menu), 6)

    # TESTS FOR RESTAURANTE
    def test_retaurante_length(self):
        TEST_LIST_RESTAURANTE = menu_api.get_menu_restaurante()
        self.assertGreaterEqual(len(TEST_LIST_RESTAURANTE), 1)
        self.assertLessEqual(len(TEST_LIST_RESTAURANTE), 10)

    def test_restaurante_date(self):
        TEST_LIST_RESTAURANTE = menu_api.get_menu_restaurante()
        for menu in TEST_LIST_RESTAURANTE:
            self.assertGreaterEqual(menu[1], time.strftime("%d-%m-%Y"))

    def test_restaurante_valid_input(self):
        try:
            menu_api.get_menu_restaurante()
        except ConnectionError:
            self.fail("Connection failed!")

    def test_restaurante_correct_values(self):
        TEST_LIST_RESTAURANTE = menu_api.get_menu_restaurante()
        for menu in TEST_LIST_RESTAURANTE:
            self.assertEqual(len(menu), 4)