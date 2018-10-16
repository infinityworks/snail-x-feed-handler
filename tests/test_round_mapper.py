import json
import unittest
import os.path
from feed import app
from feed.mappers.round_mapper import json_to_round_and_race_list

test_path = os.path.abspath(os.path.dirname(__file__))
round1_path = str(test_path) + "/test_data/rounds/round1.json"


class TestRoundMapper(unittest.TestCase):

    def test_rounds_json_to_rounds_obj_success(self):
        with open(round1_path) as f:
            data = json.load(f)
            round_id, race_list = json_to_round_and_race_list(data[0])
            print(round_id)

        self.assertTrue(True)


