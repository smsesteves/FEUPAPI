import unittest
import time
import src.menu as menu_api


class MenuTest(unittest.TestCase):

    # TESTS FOR CAFETARIA
    def test_cafetaria_length(self):
        test_list_cafetaria = menu_api.get_menu_cafetaria()
        self.assertGreaterEqual(len(test_list_cafetaria), 1)
        self.assertLessEqual(len(test_list_cafetaria), 10)

    def test_cafetaria_date(self):
        test_list_cafetaria = menu_api.get_menu_cafetaria()
        for menu in test_list_cafetaria:
            self.assertGreaterEqual(menu[1], time.strftime("%d-%m-%Y"))

    def test_cafetaria_valid_input(self):
        try:
            menu_api.get_menu_cafetaria()
        except ConnectionError:
            self.fail("Connection failed!")

    def test_cafetaria_correct_values(self):
        test_list_cafetaria = menu_api.get_menu_cafetaria()
        for menu in test_list_cafetaria:
            self.assertEqual(len(menu), 6)

    # TESTS FOR RESTAURANTE
    def test_retaurante_length(self):
        test_list_restaurante = menu_api.get_menu_restaurante()
        self.assertGreaterEqual(len(test_list_restaurante), 1)
        self.assertLessEqual(len(test_list_restaurante), 10)

    def test_restaurante_date(self):
        test_list_restaurante = menu_api.get_menu_restaurante()
        for menu in test_list_restaurante:
            self.assertGreaterEqual(menu[1], time.strftime("%d-%m-%Y"))

    def test_restaurante_valid_input(self):
        try:
            menu_api.get_menu_restaurante()
        except ConnectionError:
            self.fail("Connection failed!")

    def test_restaurante_correct_values(self):
        test_list_restaurante = menu_api.get_menu_restaurante()
        for menu in test_list_restaurante:
            self.assertEqual(len(menu), 4)