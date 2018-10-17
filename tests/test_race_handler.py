import unittest
from unittest.mock import patch

from feed.handlers.race_handler import call_race_api


class TestRaceHandler(unittest.TestCase):

    @patch("feed.handlers.race_handler")
    def test_race_handler_api_call_ok(self, mock_get):
        mock_get.return_value.status_code = 200
        response = call_race_api(1, 1)
        self.assertEqual(response.status_code, 200)
