from feed.mappers import racecard_mapper
from feed.sources import racecard_source


def write_racecard_data(race_id, snail_list):
    racecard_exists = racecard_source.check_racecard_exists(race_id)
    if not racecard_exists:
        for snail_id in snail_list:
            racecard = racecard_mapper.create_racecard_object(race_id, snail_id)
            racecard_source.save(racecard)


