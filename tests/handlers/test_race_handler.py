import unittest
from unittest.mock import patch

from feed.handlers.race_handler import call_race_api


class TestRaceHandler(unittest.TestCase):

    @patch("feed.handlers.race_handler")
    def test_race_handler_api_call_ok(self, mock_get):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViIjoxfQ" \
            ".AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"
        mock_get.return_value.status_code = 200
        response = call_race_api(1, token)
        self.assertEqual(response.status_code, 200)
