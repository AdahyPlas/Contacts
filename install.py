
from sqlite3 import *

conn = connect('database.db')

curs = conn.cursor()

curs.execute("""CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Prenom TEXT,
    Nom TEXT,
    email TEXT,
    password TEXT,
    cle TEXT
)
""")

curs.execute("""CREATE TABLE contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    proprio TEXT,
    Prenom TEXT,
    Nom TEXT,
    naissance TEXT,
    telephone TEXT,
    email TEXT,
    description TEXT

)""")