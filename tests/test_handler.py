import unittest
from feed.handlers import handler


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.token = handler.get_auth_token()

    def test_get_auth_token(self):
        token = handler.get_auth_token()
        self.assertTrue(len(token) > 0)

    # def test_get_rounds_with_auth_token(self):
    #     print(self.token)
    #     print(handler.call_round_api(self.token))
