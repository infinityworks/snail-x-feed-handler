from feed.mappers import round_mapper
from feed.sources import round_source
from feed.handlers import race_handler


def process_round_json(response_json, token):
    # try:
    print(response_json[-1])
    single_round_json = response_json[-1]
    round, race_list = round_mapper.json_to_round_and_race_list(single_round_json)
    print("Round: " + str(round))
    print("Race list: " + str(race_list))


    exists = round_source.find_one_by_id(round.id)
    if not exists and race_list:
        print("Exists: " + str(exists))
        race_list_length = len(race_list)
        print("Race list length: " + str(race_list_length))
        if race_list_length == 5:
            all_snails_added = check_five_snails(race_list, token)
            if all_snails_added:
                round_source.save(round)
                return round.id, race_list
    print("Requirements for storing round not satisfied!")
    return None, None
    # except:
    #     print("Except reached!")
    #     return None, None

def check_five_snails(race_list, token):
    for race_id in race_list:
        response = race_handler.call_race_api(race_id, token)

        response_json = response.json()
        snail_list = response_json[0]['id_snails']
        print("Snail List: " + str(snail_list))
        if len(snail_list) < 5:
            return False
    return True


def round_inflight():
    print("Round inflight: " + str(round_source.round_inflight()))
    return round_source.round_inflight()
