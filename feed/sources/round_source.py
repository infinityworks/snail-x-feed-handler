from feed.db.db_func import get_db
import datetime
from feed import db
from feed.models.round import Round


def save(round):
    db.session.add(round)
    db.session.commit()


def find_one_by_id(id):
    return Round.query.get(id)

def round_inflight():
    db = get_db()
    cursor = db.cursor()
    current_time = datetime.datetime.now()

    # THIS NEEEDS CHECKING BY AN SQL WIZARD

    query = """SELECT round.round_id
            FROM round JOIN race ON round.round_id = race.round_id 
            WHERE race.race_date = (SELECT MIN (race_date) FROM race) AND round.closed = FALSE
            AND race.race_date <= '{}' ORDER BY race.race_date ASC""".format(current_time, current_time)

    try:
        cursor.execute(query)
        db.commit()
    except db.Error:
        return False

    if cursor.fetchone():
        return True
    else:
        return False