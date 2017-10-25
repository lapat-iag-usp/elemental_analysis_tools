from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app import app, db, lm

from app.models.LoginForm import LoginForm
from app.models.User import User

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user and user.password == form.password.data:
            login_user(user)            
            flash("Logado")
            return redirect(url_for("index"))
        else:
            flash("Login Inválido")
    return render_template('login.html',form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout")
    return redirect(url_for('index'))

"""
@app.route("/profile",defaults={'username': None})
@app.route("/profile/<username>")
@login_required
def profile(username):
    return render_template('profile.html',
        username=username)
"""

"""
@app.route("/dbtest")
def dbtest():

    # insert example
    #i = User("thiagogomes","1234","bla@usp.br")
    #db.session.add(i)
    #db.session.commit()
    #return "ok"

    # select example
    #r = User.query.filter_by(username="thiagogomes").all()
    #print(r)
    #return "ok"

    # update example
    #r = User.query.filter_by(username="thiagogomes").first()
    #r.username = "pedro"
    #db.session.add(r)
    #db.session.commit()
    #return "ok"

    # delete example
    #r = User.query.filter_by(username="thiagogomes1").first()
    #db.session.delete(r)
    #db.session.commit()
    return "ok"
"""
