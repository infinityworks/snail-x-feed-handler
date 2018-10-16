from feed import db


def save_round(round):
    db.session.add(round)
    db.session.commit()
