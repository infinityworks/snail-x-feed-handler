from feed import db


class Round(db.Model):

    id = db.Column("round_id", db.Integer(), primary_key=True)
    name = db.Column("round_name", db.String(20), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    finish_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, name, start_date, end_date):
        self.id = id
        self.name = name
        self.start = start_date
        self.finish = end_date

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}>".format(self.id, self.name, self.start)

    def get_round(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_rounds(self):
        return self.query.all()
