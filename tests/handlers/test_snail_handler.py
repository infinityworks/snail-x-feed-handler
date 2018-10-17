import unittest
from unittest.mock import patch

from feed.handlers.snail_handler import call_snail_api


class TestSnailHandler(unittest.TestCase):
    @patch('feed.handlers.snail_handler')
    def test_snail_feed_handler_response_ok(self, mock_get):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDIzNzQxMjUsImlhdCI6MTUzOTc4MjEyNSwic3ViIjoxfQ" \
            ".AVC1Y0kAvfXQ1TzeTYlsuQkfBXpuyv5-SKEEZrWv8NM"
        mock_get.return_value.status_code = 200
        response = call_snail_api(1, token)
        self.assertEqual(response.status_code, 200)
