from feed.mappers.snail_mapper import json_to_snail
from feed.mappers.trainer_mapper import snail_json_to_trainer
from feed.sources import trainer_source, snail_source


def process_snail_json(snail_json):
    snail = json_to_snail(snail_json)
    trainer = snail_json_to_trainer(snail_json)

    trainer_exists = trainer_source.find_one_by_id(trainer.id)
    if not trainer_exists:
        trainer_source.save(trainer)

    snail_exists = snail_source.find_one_by_id(snail.id)
    if not snail_exists:
        snail_source.save(snail)
