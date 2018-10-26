from feed.models.round import Round


def json_to_round_and_race_list(round_json):
    race_list = round_json['races']
    round = Round(round_json['id'], round_json['name'], round_json['start_date'])
    return round, race_list
