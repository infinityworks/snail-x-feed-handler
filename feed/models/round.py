from feed import db


class Round(db.Model):

    __tablename__ = 'round'

    id = db.Column("round_id", db.Integer(), primary_key=True)
    name = db.Column("round_name", db.String(20), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    finish_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, name, start_date, finish_date):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.finish_date = finish_date

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}\n finish_date: {}>".format(self.id, self.name,
                                                                                      self.start_date, self.finish_date)

    def get_round(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_rounds(self):
        return self.query.all()
