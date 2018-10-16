from feed import db


class RaceResult(db.Model):

    id = db.Column("race_result_id", db.Integer(), primary_key=True)
    position = db.Column(db.Integer(), nullable=False)

    time_to_finish = db.Column(db.Integer(), nullable=False)
    did_not_finish = db.Column(db.Boolean(), nullable=False)
    race_participants_id = db.Column(
        db.Integer(), db.ForeignKey("race_participants.id"))

    def __repr__(self):
        return "<Race Result\nid: {}\n position: {}\n time_to_finish: {}\n did_not_finish: {}\n race_participants_id: {}>"\
            .format(self.id, self.position, self.time_to_finish, self.did_not_finish, self.id_race_participants)

    def get_race_result(self, id):
        return self.query.order_by(RaceResult.position).filter_by(race_participants_id=id).first()

    def get_all_race_results(self):
        return self.query.all()
