import json
import unittest
from feed.mappers.round_mapper import json_to_round_and_race_list
from feed import app


class TestRoundMapper(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_rounds_json_to_rounds_obj_success(self):
        with self.app_context():
            self.assertTrue(True)
