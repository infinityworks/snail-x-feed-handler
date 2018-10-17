from feed import db


def save_race(race):
    db.session.add(race)
    db.session.commit()