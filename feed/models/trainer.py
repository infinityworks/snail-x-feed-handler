from feed.db.db_setup import get_db

db = get_db()


class Trainer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Trainer\nid: {}\n name: {}>".format(self.id, self.name)

    def get_trainer(self, id):
        return self.query.filter_by(id=id).first()