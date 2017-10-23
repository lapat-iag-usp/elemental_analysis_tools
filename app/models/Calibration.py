from app import db

class Calibration(db.Model):
    __tablename__ = 'calibrations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User',foreign_keys=user_id)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<id %r>' % (self.id)
