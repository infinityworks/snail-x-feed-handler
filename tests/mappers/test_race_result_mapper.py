import unittest
import os.path
from feed.mappers.race_result_mapper import json_to_race_result

test_path = os.path.abspath(os.path.dirname(__file__))
round1_path = str(test_path) + "/test_data/results/result1.json"


class TestRaceResultMapper(unittest.TestCase):
    test_race_result_data = {
        "race_id": 2,
        "id_snail": 3,
        "position_snail": 2
    }

    def test_rounds_json_to_race_result_obj_success(self):
        race_result = json_to_race_result(self.test_race_result_data['race_id'], self.test_race_result_data)
        race_id = race_result.race_id
        snail_id = race_result.snail_id
        position = race_result.position

        self.assertEqual(race_id, self.test_race_result_data['race_id'])
        self.assertEqual(snail_id, self.test_race_result_data['id_snail'])
        self.assertEqual(position, self.test_race_result_data['position_snail'])
