from app import db

class Calibration(db.Model):
    __tablename__ = 'calibration_files'

    id = db.Column(db.Integer, primary_key=True)
    csv_path = db.Column(db.Text)
    txt_path = db.Column(db.Text)
    micromatter_id = db.Column(db.Text)

    #calibration_id = db.Column(db.Integer, db.ForeignKey('calibrations.id'))
    #user = db.relationship('Calibration',foreign_keys=calibation_id)

    def __init__(self, description,user_id):
        self.description = description
        self.calibration_id = calibration_id

    def __repr__(self):
        return '<id %r>' % (self.id)



