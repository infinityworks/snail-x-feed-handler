from feed.db.db_setup import get_db


def save_round(round):
    session = get_db()
    session.add(round)
    session.commit()
