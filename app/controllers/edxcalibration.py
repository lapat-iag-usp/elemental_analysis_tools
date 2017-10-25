from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app import app, db, lm
from werkzeug.utils import secure_filename

from app.models.EdxcalibrationForm import EdxcalibrationForm

import sys
import os
import csv

@app.route("/edxcalibration/new",methods=['GET', 'POST'])
def newEdxcalibration():
    form = EdxcalibrationForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('photos', filename))
        return redirect(url_for('index'))

    # ler csv da micromatter
    micromatter_IAGUSP = []
    with open('app/services/tests/data/calibration/micromatter_IAGUSP.csv') as linhas:
        linhascsv = csv.reader(linhas,delimiter=',')
        for linha in linhascsv:
            micromatter_IAGUSP.append(linha)

    # remove cabeçalho
    micromatter_IAGUSP.pop(0)

    return render_template('edxcalibration.html',
        form=form,
        micromatter_IAGUSP=micromatter_IAGUSP)
