import unittest
from src.auth import Auth
from src.connection_failed import ConnectionFailed


class AuthTest(unittest.TestCase):

    def test_invalid_input(self):
        auth = Auth()
        self.assertRaises(ValueError, auth.login, '', '')

    def test_url_available(self):
        try:
            auth = Auth()
            auth.login("xpto", "asdda")
        except ConnectionFailed:
            self.fail("Authentication couldn't access SIGARRA validation link!")

    def test_tries_to_authenticate(self):
        auth = Auth()
        self.assertIs(auth.login("xpto", "asdsad"), None)


