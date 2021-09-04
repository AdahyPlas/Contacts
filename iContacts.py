
from termcolor import colored
from getpass import getpass
from colorama import init
import sqlite3
from hashlib import *
from os import system
import sys
import datetime
conn = sqlite3.connect('database.db')
curs = conn.cursor()

init()

def hashdata(data):
    #hash data
    data = bytes(data, 'utf-8')
    data = sha512(data).hexdigest()
    return data

def infos(ID):
    print("\n")
    curs.execute("""SELECT * FROM contacts WHERE id=?""", (ID,))
    res = curs.fetchone()
    print(f"prénom -> {res[2]}")
    print(f"nom -> {res[3]}")
    print(f"date de naissance -> {res[4]}")
    print(f"n° de téléphone -> {res[5]}")
    print(f"adresse email -> {res[6]}")
    if res[7] == "":
        print("description -> aucune description")
    else:
        print(f"description -> {res[7]}")

def main(cle):
    listcommands = ["/exit", "/add", "/delete", "/list", "/help", "/sendKey", "/export", "/update", "/listAll", "/view"]
    while 0 != 1:
        command = input("iContacts > ")

        if command == "/exit":
            exit()

        if command == "/add":
            proprio = cle
            prenom = input("｢bot｣ Entrez le prénom de votre contact -> ")
            nom = input("｢bot｣ Entrez le nom de votre contact -> ")
            ddn = input("｢bot｣ Entrez la date de naissance de votre contact (jj/mm/aa) -> ")
            tel = input("｢bot｣ Entrez le numéro de téléphone de votre contact -> ")
            email = input("｢bot｣ Entrez l'addresse mail du contact -> ")
            descr = input("｢bot｣ Entrez une description -> ")

            curs.execute("""INSERT INTO contacts(proprio, Prenom, Nom, naissance, telephone, email, description) VALUES(?,?,?,?,?,?,?)""", (cle, prenom, nom, ddn, tel, email, descr))
            conn.commit()

        if command == "/delete":
            ID = input("Entrez le numéro de votre contact -> ")
            try:
                infos(ID)
            
                rep = input("Ce contacts ? (y/n) ")
            
                if rep == "y":
                    passwd1 = getpass("Entrez votre mot de passe -> ")
                    passwd = hashdata(passwd1)

                    curs.execute("""SELECT password FROM users WHERE cle=?""", (cle,))
                    mpdOFF = curs.fetchone()
                    mdpOFF = mpdOFF[0]
                    if passwd == mdpOFF:
                        print(colored("Le mot de passe est correct !", 'green', attrs=["bold"]))
                        curs.execute("DELETE FROM contacts WHERE id=?", (ID,))
                        conn.commit()
                        print(colored("Le contact a bien été supprimé !", 'red', attrs=["bold"]))
                    if passwd != mdpOFF:
                        print(colored("Mauvais mot de passe !", 'red', attrs=["bold"]))
                        while passwd != mdpOFF:
                            passwd1 = getpass("Entrez votre mot de passe -> ")
                            passwd = hashdata(passwd1)

                            curs.execute("""SELECT password FROM users WHERE cle=?""", (cle,))
                            mpdOFF = curs.fetchone()
                            mdpOFF = mpdOFF[0]
                            if passwd != mdpOFF:
                                print(colored("Mauvais mot de passe", 'red', attrs=["bold", "underline"]))
                            else:
                                print(colored("Le mot de passe est correct !", 'green', attrs=["bold"]))
                                curs.execute("DELETE FROM contacts WHERE id=?", (ID,))
                                conn.commit()
                                print(colored("Le contact a bien été supprimé !", 'red', attrs=["bold"]))
            except:
                print("veuillez entrez un nombre existant dans la base !")


        if command == "/list":
            curs.execute("""SELECT * FROM contacts WHERE proprio=?""", (cle,))
            rows = curs.fetchall()
            for k in rows:
                print(f"{k[0]} -> {k[2]} {k[3]} {k[4]} {k[5]} {k[6]} {k[7]}")

        if command == "/listAll":
            print("en construction")
        
        if command == "/view":
            ID = input("Entrez le numéro de votre contact -> ")
            try:
                infos(ID)
            except:
                print("Veuillez entrer un nombre existant dans la base !")

        if command == "/export":
            cleR = input("｢bot｣ Entrez la clé de la personne à qui vous envoyez le contact -> ")
            rep = input("voulez-vous exporter un contact existant y/n ")
            prenom = ""
            nom = ""
            ddn = ""
            tel = ""
            email = ""
            description = ""
            if rep == "y":
                ID = input("Entrez le numéro de la place qu'a le contact dans la base de donnée -> ")
                curs.execute("SELECT * FROM contacts WHERE id=?", (ID,))
                contact = curs.fetchone()
                prenom = contact[2]
                nom = contact[3]
                ddn = contact[4]
                tel = contact[5]
                email = contact[6]
                description = contact[7]
            if rep == "n":
            
                prenom = input("｢bot｣ Entrez le prénom du contact -> ")
                nom = input("｢bot｣ Entrez le nom du contact -> ")
                ddn = input("｢bot｣ Entrez la date de naissance du contact -> ")
                tel = input("｢bot｣ Entrez le numéro de téléphone du contact -> ")
                email = input("｢bot｣ Entrez l'adresse mail du contact -> ")
                description = input("｢bot｣ Entrez un description pour le contact -> ")

            if description == "":
                description = "/"
            cmd = f'curs.execute("""INSERT INTO contacts(proprio, Prenom, Nom, naissance, telephone, email, description) VALUES("{cleR}", "{prenom}", "{nom}", "{ddn}", "{tel}", "{email}", "{description}")""")'


            fichier = open('ToSend.py', 'w')

            sys.stdout = fichier


            print("import sqlite3")
            print("conn = sqlite3.connect('database.db')")
            print("curs = conn.cursor()")
            print(cmd)
            print("conn.commit()")
            print("conn.close()")

            sys.stdout = sys.__stdout__
            fichier.close()


        if command == "/sendKey":
            print(cle)

        if command == "/update":
           print("en construction")


        if command == "/help":
            print("/exit -> quitte le programme")
            print("/add -> ajoute un contact")
            print("/delete -> supprime un contact")
            print("/list -> affiche tout les contacts")




        if command in listcommands:
            continue
        elif command == " ":
            print(colored("Veuillez entrer une commande", 'red', attrs=["bold"]))

        elif command == "":
            print(colored("Veuillez entrer une commande", 'red', attrs=["bold"]))
        else:
            print(colored(f"La commande {command} n'a pas été trouvée", 'red', attrs=["bold"]))








    conn.close()
