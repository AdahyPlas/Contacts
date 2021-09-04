
from colorama import init
from termcolor import colored
from hashlib import *
from sqlite3 import *
from getpass import getpass
from iContacts import main
from random import sample


init()

alp = "abcdefghijklmnopqrstuvwxyz"
ALP = alp.upper()
chiffres = "0123456789"
all = alp+ALP+chiffres
conn = connect("database.db")
curs = conn.cursor()

def hashdata(data):
    #hash data
    data = bytes(data, 'utf-8')
    data = sha512(data).hexdigest()
    return data

def ChangeMDP():
    email1 = input("｢bot｣ Entrez votre addresse email -> ") #demande de l'email
    email = hashdata(email1)
    curs.execute("""SELECT email FROM users WHERE email=?""", (email, ))
    emailOFF = curs.fetchone()
    if emailOFF == None:
        print(colored(f"{email1} n'a pas été trouvé dans la base de donnée", 'red', attrs=["bold"]))
        exit()
    cleUSER1 = input("｢bot｣ Entrez votre clé (elle contient 62 caractères) -> ") #demande de la clé
    cleUSER = hashdata(cleUSER1)
    curs.execute("""SELECT cle FROM users WHERE email=?""", (email,)) #requête sql pour obtenir la clé enregistréé
    cleOFF = curs.fetchone()
    cleOFFCICIAL = cleOFF[0]


    if cleUSER == cleOFFCICIAL: #vérification des clés
        print(colored("Les clés sont identiques", 'green', attrs=["bold"]))
    elif cleUSER != cleOFFCICIAL:
        print(colored("｢bot｣ Les clé ne correspondent pas !", 'red', attrs=["bold"]))
        while cleUSER != cleOFFCICIAL:
            cleUSER1 = input(colored("｢bot｣ Entrez votre clé (elle contient 62 caractères) -> ", 'red', attrs=["bold"]))
            cleUSER = hashdata(cleUSER1)
            if cleUSER != cleOFFCICIAL:
                print(colored("Les clés ne sont pas identiques", 'red', attrs=["bold"]))
        print(colored("Les clés sont identiques", 'green', attrs=["bold"]))

    mdp1 = getpass("｢bot｣ Entrez votre nouveau Mot De Passe -> ") #demande du nouveau mot de passe
    mdp2 = getpass("｢bot｣ Réentrez votre mot de passe -> ") #redemande du nouveau mot de passe

    if mdp2 != mdp1: #vérification que les mot de passes soien identiques
        print(colored("Les mot de passes ne correspondent pas !", 'red', attrs=["bold"]))
        while mdp2 != mdp1:
            mdp2 = input(colored("Les mot de passes ne correspondent pas !", 'red', attrs=["bold"]))
            if mdp1 != mdp2:
                print(colored("Les mot de passes ne correspondent pas !", 'red', attrs=["bold"]))

    print(colored("Les mot de passes sont identiques !", 'green', attrs=["bold"]))
    mdp2 = bytes(mdp2, 'utf-8')
    mdp2 = sha512(mdp2).hexdigest()
    curs.execute("""UPDATE users SET password=? WHERE email=?""", (mdp2, email)) #enregistrement du nouveau mot de passe dans la base de donnée
    conn.commit()

def connection():
    email1 = input("｢bot｣ Entrez votre adresse mail -> ")
    email = hashdata(email1)

    curs.execute("""SELECT email FROM users WHERE email=?""", (email,))
    verif = curs.fetchone()
    if verif == None:
        print(colored(f"｢bot｣ {email1} n'a pas été trouvé dans la base de donnée !", 'red', attrs=["bold"]))
        while verif == None:
            email1 = input(colored("｢bot｣ Entrez votre adresse mail -> ", 'red', attrs=["bold"]))
            email = hashdata(email1)

            curs.execute("""SELECT email FROM users WHERE email=?""", (email,))
            verif = curs.fetchone()

            if verif == None:
                print(colored(f"｢bot｣ {email1} n'a pas été trouvé dans la base de donnée !", 'red', attrs=["bold"]))

    cle1 = input("｢bot｣ Entrez votre clé d'identification -> ")
    cle = hashdata(cle1)

    curs.execute("""SELECT cle FROM users WHERE email=?""", (email, ))
    cleOFF = curs.fetchone()

    cleOFF = cleOFF[0]

    if cle != cleOFF:
        print(colored("Les clés ne correspondent pas !", 'red', attrs=["bold"]))
        quest = input("Voulez-vous recommencer ? (Y/N) ")
        if quest == "Y":
            while cle != cleOFF:
                email1 = input("｢bot｣ Entrez votre adresse mail -> ")
                email = hashdata(email1)
                cle1 = input("｢bot｣ Entrez votre clé d'identification -> ")
                cle = hashdata(cle1)
                curs.execute("""SELECT cle FROM users WHERE email=?""", (email, ))
                cleOFF = curs.fetchone()
                cleOFF = cleOFF[0]

                if cle != cleOFF:
                    print(colored("Les clés ne correspondent pas !", 'red', attrs=["bold"]))

    


    main(cleOFF)

def add():
    prenom1 = input("｢bot｣ entrez votre prénom -> ")
    prenom = hashdata(prenom1)

    nom1 = input("｢bot｣ entrez votre nom de famille -> ")
    nom = hashdata(nom1)

    email1 = input("｢bot｣ entrez votre adresse email -> ")
    email1 = email1.lower()
    email = hashdata(email1)

    curs.execute("""SELECT email FROM users WHERE email=?""", (email,))
    emails = curs.fetchone()
    if emails != None:
        print("Cette adresse mail est déjà enregistrée dans la base de donnée")
        rep1 = input("voulez-vous quitter ou pas ? Y/N ")
        if rep1 == "N":
            rep = input("Vous souvenez-vous de votre mot de passe ? (Y/N) ")
            if rep == "Y":
                connection()
            else:
                ChangeMDP()
        else:
            exit()
    else:

        mdp1 = getpass("｢bot｣ entrez votre mot de passe -> ")
        mdp2 = getpass("｢bot｣ entrez encore un fois votre mot de passe -> ")

        if mdp1 == mdp2:
            print(colored("les mot de passes sont identiques !", 'green', attrs=["bold"]))
            mdp2cd  = hashdata(mdp2)

        cle1 = "".join(sample(all, 62))
        cle = hashdata(cle1)
        curs.execute("""SELECT cle FROM users WHERE cle=?""", (cle,))
        resultat = curs.fetchone()

        if resultat != None:
            while resultat != None:
                cle1 = "".join(sample(all, 62))
                cle = hashdata(cle1)
                curs.execute("""SELECT cle FROM users WHERE cle=?""", (cle,))
                resultat = curs.fetchall()


        print(colored("votre clé est", 'red', attrs=["bold", "underline"]) + " " + cle1 + " " + colored("elle vous servira à changer votre mot de passe, etc. Ne l'a donnez à personne !", 'red', attrs=["bold", "underline"]))

        curs.execute("""INSERT INTO users(Prenom, Nom, email, password, cle) VALUES(?,?,?,?,?)""", (prenom, nom, email, mdp2, cle))
        conn.commit()
