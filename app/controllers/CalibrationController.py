from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app import app, db, lm
from werkzeug.utils import secure_filename

from app.models.Calibration import Calibration
from app.models.User import User

from app.models.forms.CalibrationForm import CalibrationForm, CalibrationFormFiles

import sys
import os
import csv

@app.route("/calibration/new",methods=['GET', 'POST'])
@login_required
def newCalibration():
    form = CalibrationForm()
    if form.validate_on_submit():
        description = form.description.data
    
        # TEST
        user = User.query.filter_by(username='admin').first()

        # save in database
        x = Calibration(description=description,user_id=1)
        #x.user.append(user)
        db.session.add(x)
        db.session.commit()

        #print(description)
#        f = form.photo.data
#        filename = secure_filename(f.filename)
#        f.save(os.path.join('photos', filename))
        return redirect(url_for('indexCalibration'))

    # ler csv da micromatter
    micromatter_IAGUSP = []
    with open('app/services/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
        linhascsv = csv.reader(linhas,delimiter=',')
        for linha in linhascsv:
            micromatter_IAGUSP.append(linha)

    # remove cabeçalho
    micromatter_IAGUSP.pop(0)

    return render_template('calibration/new.html',
        form=form,
        micromatter_IAGUSP=micromatter_IAGUSP)

@app.route("/calibration/index",methods=['GET', 'POST'])
@login_required
def indexCalibration():
    calibrations = Calibration.query.all()
    return render_template('calibration/index.html',
        calibrations=calibrations)

@app.route("/calibration",defaults={'id': 0})
@app.route("/calibration/<id>")
@login_required
def showCalibration(id):
    form = CalibrationFormFiles()
    calibration = Calibration.query.filter_by(id=id).first()
    return render_template('calibration/show.html',
            calibration=calibration,
            form=form)
