from feed.sources.round_source import *
from feed.models.round import Round


def save(round):
    save_round(round)
    return round.id


def check_round_exists(latest_round):
    return Round.query.filter_by(id=latest_round.id).first()

