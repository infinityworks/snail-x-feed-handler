from feed.mappers import race_result_mapper
from feed.sources import race_result_source


def process_race_result_json(response_json):
    return
    # for single_race_result in response_json:
    #
    # race_result_list = race_result_mapper.json_to_race_result_list(response_json)
    #
    #
    # # exists = round_source.find_one_by_id(round.id)
    # # if not exists:
    # #     round_source.save(round)
    # #     return round.id, race_list
    # # else:
    # #     print("exists")
    # #     return None, None
