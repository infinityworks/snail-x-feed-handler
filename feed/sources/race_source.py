from feed import db
from feed.models.race import Race


def save(race):
    db.session.add(race)
    db.session.commit()

# def update(race):
#     new_race = db.session.query().filter_by(id = race.id).first()


def find_one_by_id(id):
    return Race.query.get(id)

