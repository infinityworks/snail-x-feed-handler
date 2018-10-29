import unittest
from unittest.mock import patch

from feed.handlers.race_result_handler import call_race_result_api


class TestRaceResultHandler(unittest.TestCase):

    @patch("feed.handlers.race_result_handler")
    def test_call_race_result_api_response_ok(self, mock_get):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViIjoxfQ" \
                ".AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"
        mock_get.return_value.status_code = 200
        response = call_race_result_api(token)
        self.assertEqual(response.status_code, 200)
