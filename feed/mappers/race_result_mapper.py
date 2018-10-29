from feed.models.race_result import RaceResult


def json_to_race_result(race_id, race_result_json):

    race_result = RaceResult(race_id, race_result_json['id_snail'], race_result_json['position_snail'])
    return race_result