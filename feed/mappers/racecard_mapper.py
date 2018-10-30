from feed.models.racecard import Racecard


def create_racecard_object(race_id, snail_id):
    racecard = Racecard(race_id, snail_id)
    return racecard
