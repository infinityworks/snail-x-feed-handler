import sqlalchemy
from feed.db.db_setup import get_db

db = get_db()

class Round(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}>".format(self.id, self.name, self.start_date)

    def get_round(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_rounds(self):
        return self.query.all()