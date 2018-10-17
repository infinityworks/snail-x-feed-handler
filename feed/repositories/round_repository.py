from feed.mappers import round_mapper
from feed.sources import round_source


def process_round_json(response_json):
    single_round_json = response_json[:-1][0]
    round, race_list = round_mapper.json_to_round_and_race_list(single_round_json)

    exists = round_source.find_one_by_id(round.id)
    if not exists:
        round_source.save(round)
        return round.id, race_list
    else:
        print("exists")
        return None, None
