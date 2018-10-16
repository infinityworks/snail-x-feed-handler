from feed import db


class Snail(db.Model):

    id = db.Column("snail_id", db.Integer, primary_key=True)
    name = db.Column("snail_name", db.String(50), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))

    def __repr__(self):
        return "<Snail\nid: {}\n name: {}\n trainer_id: {}>".format(self.id, self.name, self.trainer_id)

    def get_snail(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_snails(self):
        return self.query.all()