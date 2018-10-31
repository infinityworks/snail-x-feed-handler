from feed import db


class RoundResult(db.Model):
    __tablename__ = "roundresult"

    id = db.Column("round_result_id", db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    round_id = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer(), nullable=False)

    def __init__(self, user_id, round_id, score):
        self.user_id = user_id
        self.round_id = round_id
        self.score = score

    def __repr__(self):
        return "<Roundresult\nid: {}\n user_id: {}\n round_id: {}\n score: {}>".format(self.id, self.user_id,
                                                                                       self.round_id, self.score)

    def get_racecard(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_racecards(self):
        return self.query.all()
