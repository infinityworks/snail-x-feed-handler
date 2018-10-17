import unittest
import os.path
from feed.mappers.race_mapper import json_to_race_and_snail_list

test_path = os.path.abspath(os.path.dirname(__file__))
race1_path = str(test_path) + "/test_data/races/singlerace1.json"


class TestRoundMapper(unittest.TestCase):

    test_race_data = {
        "id": 1,
        "date": "Thu, 11 Oct 2018 10:47:00 GMT",
        "status": "Started",
        "id_round": 1,
        "id_snails": [1, 2, 3]
    }

    def test_race_json_to_race_obj_success(self):
        race, snail_list = json_to_race_and_snail_list(self.test_race_data)
        race_id = race.id

        self.assertEqual(race_id, self.test_race_data['id'])
        self.assertEqual(len(snail_list), len(self.test_race_data['id_snails']))

