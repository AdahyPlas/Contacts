
#!-*- Encoding:Utf-8 -*-
"""
main.py

Created by Adahy on 2021-06-11.
Copyright (c) 2021 APJCMMOL. Al right reserved
"""
from functions import *
print("    _ ______            __             __ ")
print("   (_) ____/___  ____  / /_____ ______/ /_")
print("  / / /   / __ \/ __ \/ __/ __ \`/ ___/ __/")
print(" / / /___/ /_/ / / / / /_/ /_/ / /__/ /_  ")
print("/_/\____/\____/_/ /_/\__/\__,_/\___/\__/  ")
print("                                          ")
print("\n")

print("｢auteur｣ Adahy Plas")
print("｢github｣ PhilHarmonic")
print("")
def main():
    print("｢1｣ Se connecter")
    print("｢2｣ J'ai oublié mes identifiants")
    print("｢3｣ Créer un nouveau compte")
    print("｢4｣ annuler")

    rep1 = input("Entrez votre choix -> ")

    if rep1 == "1":
        connection()

    if rep1 == "2":
        ChangeMDP()

    if rep1 == "3":
        add()

    if rep1 == "4":
        print("｢exit｣")
        exit()

def execute():
    try:
        while 0 != 1:
            main()
    except KeyboardInterrupt:
        print("\n")
        rep = input("Voulez-vous terminer le programme (y/n) -> ")
        if rep == "y":
            print("\n")
            print("fermeture de la base de donnée")
            conn.close()
            print("La base est fermée")
            exit()
        elif rep ==  "n":
            execute()

if __name__ == '__main__':
    execute()
