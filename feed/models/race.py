import sqlalchemy
from feed.db.db_setup import get_db

db = get_db()

class Race(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    id_round = db.Column(db.Integer(), db.ForeignKey("round.id"))

    def __repr__(self):
        return "<Race\nid: {}\n date: {}\n status: {}\n round_id: {}>".format(self.id, self.date, self.status,
                                                                              self.id_round)

    def get_race(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_races(self):
        return self.query.all()

    def get_round_race_ids(self, id_round):
        return db.session.query(Race.id).filter_by(id_round=id_round).all()