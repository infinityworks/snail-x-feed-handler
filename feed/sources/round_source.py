from feed import db


def save_round(round):
    session = db
    session.add(round)
    session.commit()
