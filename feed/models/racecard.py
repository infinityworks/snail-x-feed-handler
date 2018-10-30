from feed import db


class Racecard(db.Model):

    id = db.Column("race_card_id", db.Integer(), primary_key=True)
    race_id = db.Column(db.Integer(), nullable=False)
    snail_id = db.Column(db.Integer(), nullable=False)


    def __init__(self, race_id, snail_id):
        self.race_id = race_id
        self.snail_id = snail_id

    def __repr__(self):
        return "<Racecard\nid: {}\n race_id: {}\n snail_id: {}>".format(self.id, self.race_id, self.snail_id)

    def get_racecard(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_racecards(self):
        return self.query.all()
