from feed.mappers import round_mapper
from feed.sources import round_source
from feed.models.round import Round


def process_round_json(response_json):
    single_round_json = response_json[:-1][0]
    round, race_list = round_mapper.json_to_round_and_race_list(single_round_json)

    exists = check_round_exists(round)

    # # if we dont, process it, otherwise leave it
    if not exists:
        round_id = round_source.save_round(round)
        return round_id, race_list
        # process races
    else:
        # ignore
        print("exists")
        return None, None


def check_round_exists(latest_round):
    return Round.query.filter_by(id=latest_round.id).first()
