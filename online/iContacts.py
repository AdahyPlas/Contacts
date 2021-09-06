from sqlite3 import *
from flask import *
from hashlib import *

conn = connect("../database.db")
curs = conn.cursor()

app = Flask(__name__)

def hashdata(data):
    #hash data
    data = bytes(data, 'utf-8')
    data = sha512(data).hexdigest()
    return data
@app.route("/")
def acc():
    return "hello"
@app.route('/connexion')
def connexion():
    return render_template("connexion.html")

@app.route('/iContacts', methods = ['GET'])
def iContacts():
    resultat = request.args
    mail = resultat["Addr"].lower()
    mail = hashdata(mail)
    Key = resultat["Key"]
    Key = hashdata(Key)
    return render_template("iContacts.html", mail=mail, key=Key)
app.run(host="192.168.1.7", port=1313, debug=True)
