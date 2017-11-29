from app import db

class Calibration(db.Model):
    __tablename__ = 'calibrations'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',foreign_keys=user_id)

    def __init__(self, description,user_id):
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return '<id %r>' % (self.id)



