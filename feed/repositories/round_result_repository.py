from feed.sources import race_predictions_source, race_result_source, round_result_source
from feed.mappers import round_result_mapper


def calc_and_store_round_results(round_id):
    round_user_ids = get_round_user_ids(round_id)

    print("**************** round_user_ids: " + str(round_user_ids))
    for user_id in round_user_ids:
        # user_predictions stores a list of race_id:snail_id dictionaries, denoting which they predicted would win
        user_predictions = race_predictions_source.get_predictions_by_user_id(user_id)
        print("****** user_predictions: " + str(user_predictions))

        # relevant_race_results stores a list of the position their snail came in
        relevant_race_results = race_result_source.get_relevant_results(user_predictions)
        print("******* relevant race results: " + str(relevant_race_results))

        # calculates the user's score for this round
        score = calculate_user_score(relevant_race_results)
        print("***** score: " + str(score))

        # creates a round_result object and saves to the db using this object
        round_result = round_result_mapper.create_round_result_object(user_id, round_id, score)
        print("*** round_result_object; " + str(round_result))
        round_result_source.save(round_result)


def get_round_user_ids(round_id):
    # round_user_id_tuples stores a list of tuples containing each of the participating users' ids.
    round_user_id_tuples = race_predictions_source.get_round_user_ids(round_id)

    round_user_ids = []
    for round_user_id_tuple in round_user_id_tuples:
        round_user_ids.append(round_user_id_tuple[0])
    return round_user_ids


def calculate_user_score(relevant_race_results):
    score = 0
    for race_result in relevant_race_results:
        if race_result[0] == 1:
            score += 5
        elif race_result[0] == 2:
            score += 3
        elif race_result[0] == 3:
            score += 1
    return score
