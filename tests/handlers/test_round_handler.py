import unittest
from unittest.mock import patch

from feed.handlers.round_handler import call_round_api


class TestRoundHandler(unittest.TestCase):

    @patch("feed.handlers.round_handler")
    def test_call_round_api_response_ok(self, mock_get):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViIjoxfQ" \
            ".AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"
        mock_get.return_value.status_code = 200
        response = call_round_api(token)
        self.assertEqual(response.status_code, 200)