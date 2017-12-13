import sys
import os

from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required,current_user
from app import app, db, lm
from werkzeug.utils import secure_filename

from app.models.Calibration import Calibration
from app.models.CalibrationFiles import CalibrationFiles
from app.models.User import User

from app.models.forms.CalibrationForm import CalibrationForm, CalibrationFormFiles

from app.scripts.Micromatter import getSample

@app.route("/calibration/new",methods=['GET', 'POST'])
@login_required
def newCalibration():
    print()
    form = CalibrationForm()
    if form.validate_on_submit():

        # save in database
        calibration_data = Calibration(
            description = form.description.data,
            user_id = current_user.get_id()
        )
        db.session.add(calibration_data)
        db.session.commit()

        return redirect(url_for('showCalibration',id=calibration_data.id))

    return render_template('calibration/new.html',
        form=form
    )

@app.route("/calibration/index",methods=['GET', 'POST'])
@login_required
def indexCalibration():
    calibrations = Calibration.query.all()
    return render_template('calibration/index.html',
        calibrations=calibrations)

@app.route("/calibration",defaults={'id': 0})
@app.route("/calibration/<id>",methods=['GET', 'POST'])
@login_required
def showCalibration(id):
    form = CalibrationFormFiles()
    calibration = Calibration.query.filter_by(id=id).first()

    if form.validate_on_submit():
        begin = 'micromatter' + str(form.micromatter_id.data) + '_' + 'calibration_' + str(calibration.id) + '_'
        # csv
        csv_filename = begin + secure_filename(form.csv_file.data.filename)
        form.csv_file.data.save(os.path.join('files', csv_filename))

        # txt
        txt_filename = begin + secure_filename(form.txt_file.data.filename)
        form.txt_file.data.save(os.path.join('files', txt_filename))

        calibration_files_data = CalibrationFiles(
            csv_file = csv_filename,
            txt_file = txt_filename, 
            micromatter_id = form.micromatter_id.data, 
            calibration_id = calibration.id
        )
        db.session.add(calibration_files_data)
        db.session.commit()

        return redirect(url_for('showCalibration',id=calibration.id))

    # get all uploaded files from this calibration
    uploads = CalibrationFiles.query.filter_by(calibration_id=calibration.id).all()
    
    # adding micrommater info
    info = {}
    for i in uploads:
        info[i.micromatter_id] = getSample(i.micromatter_id)
    
    return render_template('calibration/show.html',
            calibration=calibration,
            form=form,
            info=info,
            uploads = uploads
    )
