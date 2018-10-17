import unittest
from feed.mappers.snail_mapper import json_to_snail


class TestSnailMapper(unittest.TestCase):
    test_snail_data = {
        "id": 1,
        "name": "JSnail",
        "trainer": {
            "id": 1,
            "name": "Junaid"
        }
    }

    def test_snail_json_to_snail_obj_success(self):
        snail = json_to_snail(self.test_snail_data)

        self.assertEqual(snail.id, self.test_snail_data['id'])
