import requests
import connection_failed as ConnectionFailed


class Auth:
    def __init__(self):
        pass

    def login(self, username, password):

        if len(username) == 0:
            raise ValueError()

        if len(password) == 0:
            raise ValueError()

        url = "https://sigarra.up.pt/feup/pt/vld_validacao.validacao"
        data = {
            'p_user': username,
            'p_pass': password
        }

        response = requests.post(url, data)

        if response.status_code != requests.codes.ok:
            raise ConnectionFailed

        for key in ['SI_SECURITY', 'SI_SESSION']:
            if response.cookies.get(key) is None or response.cookies.get(key) == 0:
                return None

        return response.cookies.get_dict()
