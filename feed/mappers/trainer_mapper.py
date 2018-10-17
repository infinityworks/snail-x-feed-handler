from feed.models.trainer import Trainer


def snail_json_to_trainer(snail_json):
    trainer_json = snail_json["trainer"]
    trainer = Trainer(trainer_json["id"], trainer_json["name"])
    return trainer
