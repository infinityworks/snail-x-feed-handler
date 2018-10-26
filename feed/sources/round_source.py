import datetime
from feed import db
from feed.models.round import Round


def save(round):
    db.session.add(round)
    db.session.commit()


def find_one_by_id(id):
    return Round.query.get(id)

def round_inflight():
    current_time = datetime.datetime.now()
    result = db.engine.execute("SELECT round.round_id FROM round JOIN race ON round.round_id = race.round_id WHERE race.race_date = (SELECT MIN (race_date) FROM race) AND round.closed = FALSE AND race.race_date <= '{}' ORDER BY race.race_date ASC".format(current_time))
    inflight_round = result.fetchone()
    if inflight_round:
        return True
    else:
        return False

def is_final_race(race_id):
    query = "SELECT round.round_id FROM round JOIN race ON round.round_id = race.round_id WHERE race.race_date = (SELECT MAX (race_date) FROM race) AND race.race_id = '{}'".format(race_id)
    query_result = db.engine.execute(query)
    is_final_race = query_result.fetchone()
    if is_final_race:
        return True
    else:
        return False