from feed.models.race import Race


def json_to_race_and_snail_list(race_json):
    snail_list = race_json['id_snails']
    race = Race(race_json['id'], race_json['date'], race_json['status'], race_json['id_round'])
    return race, snail_list