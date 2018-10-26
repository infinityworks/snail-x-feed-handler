from feed import db


class RaceResult(db.Model):

    __tablename__ = "raceresult"

    id = db.Column("race_result_id", db.Integer(), primary_key=True)
    race_id = db.Column(db.Integer(), db.ForeignKey("race.race_id"))
    snail_id = db.Column(db.Integer(), db.ForeignKey("snails.snail_id"))
    position = db.Column(db.Integer(), nullable=False)

    def __init__(self, race_id, snail_id, position):
        self.race_id = race_id
        self.snail_id = snail_id
        self.position = position

    def __repr__(self):
        return "<Race Result\nid: {}\n race_id: {}\n snail_id: {}\n position: {}>"\
            .format(self.id, self.race_id, self.snail_id, self.position)

    def get_race_result(self, id):
        return self.query.order_by(RaceResult.position).filter_by(snail_id=id).first()

    def get_all_race_results(self):
        return self.query.all()
