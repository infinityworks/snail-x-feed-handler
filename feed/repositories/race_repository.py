from feed.mappers import race_mapper
from feed.sources import race_source


def process_race_json(response_json):
    single_race_json = response_json[0]
    race, snail_list = race_mapper.json_to_race_and_snail_list(single_race_json)

    exists = race_source.find_one_by_id(race.id)
    if not exists:
        race_source.save(race)

    return race, snail_list
