from feed import db


class Racecard(db.Model):

    id = db.Column("race_card_id", db.Integer(), primary_key=True)
    race_id = db.Column(db.Integer(), nullable=False)
    snail_id = db.Column(db.Integer(), nullable=False)


    def __init__(self, id, date, status, round_id):
        self.id = id
        self.date = date
        self.status = status
        self.round_id = round_id

    def __repr__(self):
        return "<Race\nid: {}\n date: {}\n status: {}\n round_id: {}>".format(self.id, self.date, self.status,
                                                                              self.round_id)

    def get_race(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_races(self):
        return self.query.all()

    def __repr__(self):
        return "<Race Result\nid: {}\n position: {}\n time_to_finish: {}\n did_not_finish: {}\n race_participants_id: {}>"\
            .format(self.id, self.position, self.time_to_finish, self.did_not_finish, self.id_race_participants)

    def get_race_result(self, id):
        return self.query.order_by(RaceResult.position).filter_by(race_participants_id=id).first()

    def get_all_race_results(self):
        return self.query.all()
