from sqlite3 import *
from flask import *

conn = connect("../database.db")
curs = conn.cursor()

app = Flask(__name__)

@app.route("/")
def acc():
    return "hello"
@app.route('/connexion')
def connexion():
    return render_template("connexion.html")

@app.route('/iContacts', methods = ['POST'])
def iContacts():
    return "hello"

app.run(host="192.168.1.7", port=1313, debug=True)