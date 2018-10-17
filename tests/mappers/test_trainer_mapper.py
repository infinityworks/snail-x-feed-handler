import unittest
from feed.mappers.trainer_mapper import snail_json_to_trainer


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
        trainer = snail_json_to_trainer(self.test_snail_data)

        self.assertEqual(trainer.id, self.test_snail_data['trainer']['id'])
