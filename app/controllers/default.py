from app import app

@app.route("/")
def index():
    return "Testing route"

@app.route("/calibration/<int:id>",methods=['GET'])
def calibration(id):
    return "calibration number %s" % str(id)

@app.route("/profile",defaults={'username': None})
@app.route("/profile/<username>")
def profile(username):
    if username:
        return "Hello %s" % username
    else:
        return "Olá desconehcido"


