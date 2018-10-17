import unittest

from unittest.mock import patch

from feed.handlers import token_handler


class TestTokenHandler(unittest.TestCase):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViIjoxfQ" \
            ".AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"

    token_json = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViI" \
                 "joxfQ.AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"
    }

    @patch('feed.handlers.token_handler')
    def test_call_auth_api(self, mock_get):
        mock_get.return_value.status_code = 200
        response = token_handler.call_auth_api()
        self.assertEqual(response.status_code, 200)

    @patch('feed.handlers.token_handler')
    def test_get_auth_token(self, mock_get):
        mock_get.return_value = self.token
        response = token_handler.get_auth_token_from_response(self.token_json)
        self.assertEqual(response, self.token)
