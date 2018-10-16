from feed import db


class Race(db.Model):

    id = db.Column("race_id", db.Integer(), primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    round_id = db.Column(db.Integer(), db.ForeignKey("round.id"))

    def __init__(self, id, date, status, id_round):
        self.id = id
        self.date = date
        self.status = status
        self.id_round = id_round

    def __repr__(self):
        return "<Race\nid: {}\n date: {}\n status: {}\n round_id: {}>".format(self.id, self.date, self.status,
                                                                              self.round_id)

    def get_race(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_races(self):
        return self.query.all()

    @staticmethod
    def get_round_race_ids(round_id):
        return db.session.query(Race.id).filter_by(id_round=round_id).all()
