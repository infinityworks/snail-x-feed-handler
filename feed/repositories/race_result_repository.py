from feed.mappers import race_result_mapper
from feed.sources import race_result_source, round_source


def process_race_result_json(response_json):
    print(response_json)
    final_race_resulted = False
    for single_race_results in response_json:
        race_id = single_race_results['id_race']
        result_exists = race_result_source.check_race_resulted(race_id)
        print("Result exists; " + str(result_exists))

        if not result_exists:
            # Check whether it's the final race in the round, if so changes closed status from false to true and returns true
            final_race_resulted = round_source.is_final_race(race_id)
            # Adds the race_result to the db
            individual_results = single_race_results['snails']
            for race_result_json in individual_results:
                race_result = race_result_mapper.json_to_race_result(race_id, race_result_json)
                race_result_source.save(race_result)

    return final_race_resulted
