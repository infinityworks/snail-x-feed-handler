from feed.mappers import race_mapper
from feed.sources import race_source
from feed.models.race import Race


def process_race_json(response_json):
    single_race_json = response_json[0]
    race, snail_list = race_mapper.json_to_race_and_snail_list(single_race_json)
    race_source.save_race(race)
    return race, snail_list

    