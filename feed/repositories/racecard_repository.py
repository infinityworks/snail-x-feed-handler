from feed.mappers import racecard_mapper
from feed.sources import racecard_source


def write_racecard_data(race_id, snail_list):
    for snail_id in snail_list:
        racecard = racecard_mapper.create_racecard_object(race_id, snail_id)

        racecard_exists = racecard_source.find_one_by_id(racecard.id)
