import json
import unittest
import os.path
from feed.mappers.round_mapper import json_to_round_and_race_list

test_path = os.path.abspath(os.path.dirname(__file__))
round1_path = str(test_path) + "/test_data/rounds/round1.json"


class TestRoundMapper(unittest.TestCase):

    data = {
        "id": 1,
        "name": "External",
        "start_date": "Mon, 01 Oct 2018 10:00:00 GMT",
        "end_date": "Mon, 01 Oct 2018 12:00:00 GMT",
        "races": [1, 2, 3]
    }

    def test_rounds_json_to_rounds_obj_success(self, data):
        round, race_list = json_to_round_and_race_list(data)
        round_id = round.id
        
        self.assertEqual(round_id, data['id'])


