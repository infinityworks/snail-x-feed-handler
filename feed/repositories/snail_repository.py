from feed.mappers.snail_mapper import json_to_snail
from feed.mappers.trainer_mapper import snail_json_to_trainer
from feed.sources import trainer_source, snail_source


def process_snail_json(snail_json):
    snail = json_to_snail(snail_json)
    trainer = snail_json_to_trainer(snail_json)

    if not trainer_source.find_one_by_id(trainer.id):
        trainer_source.save(trainer)

    if not snail_source.find_one_by_id(snail.id):
        snail_source.save(snail)

    print("DONE (Snail Processed - " + str(snail))

