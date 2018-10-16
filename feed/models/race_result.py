from feed.db.db_setup import get_db

db = get_db()


class RaceResult(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    position = db.Column(db.Integer(), nullable=False)

    time_to_finish = db.Column(db.Integer(), nullable=False)
    did_not_finish = db.Column(db.Boolean(), nullable=False)
    id_race_participants = db.Column(
        db.Integer(), db.ForeignKey("race_participants.id"))

    def __repr__(self):
        return "<Race Result\nid: {}\n position: {}\n time_to_finish: {}\n did_not_finish: {}\n race_participants_id: {}>"\
            .format(self.id, self.position, self.time_to_finish, self.did_not_finish, self.id_race_participants)

    def get_race_result(self, id):
        return self.query.order_by(RaceResult.position).filter_by(id_race_participants=id).first()

    def get_all_race_results(self):
        return self.query.all()
