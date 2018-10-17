from feed import db


class Trainer(db.Model):

    __tablename__ = "trainers"

    id = db.Column("trainer_id", db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Trainer\nid: {}\n name: {}>".format(self.id, self.name)

    def get_trainer(self, id):
        return self.query.filter_by(id=id).first()