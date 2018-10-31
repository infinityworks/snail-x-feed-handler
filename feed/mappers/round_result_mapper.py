from feed.models.round_result import RoundResult


def create_round_result_object(user_id, round_id, score):

    round_result = RoundResult(user_id, round_id, score)
    return round_result