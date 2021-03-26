from random import choice
from dessinPendu import dessinPendu

mot = choice(open('dico.txt', 'r').read().splitlines())
lettres_trouve, lettres_incorrect = [], []
erreurs = 0


def afficher_mot():
    mot_affichable = ""
    for lettre in mot:
        if lettre in lettres_trouve:
            mot_affichable += lettre
        else:
            mot_affichable += "-"
    print(mot_affichable)


def verifier_lettre(lettre):
    global erreurs

    if len(lettre) > 1:
        print("Désolé,vous devez entrer une seule lettre")

    lettre_majuscule = lettre.upper()
    if lettre_majuscule in lettres_trouve:
        print("Cette lettre est correcte")
        print("Faites attention, vous avez déja proposé cette lettre")
        return

    for i in range(len(mot)):
        if mot[i] == lettre_majuscule:
            lettres_trouve.append(lettre_majuscule)
            print("Cette lettre est correcte")
            return

    print("Cette lettre est incorrecte")
    erreurs += 1
    if lettre in lettres_incorrect:
        print("En plus, vous avez déja proposé cette lettre !")
    else:
        lettres_incorrect.append(lettre)


def afficher_pendu():
    print(dessinPendu(erreurs))


def boucle_pendu():
    lettres_mot = []
    for lettre in mot:
        if lettre in lettres_trouve:
            lettres_mot.append(lettre)

    return (len(lettres_mot) == len(mot)) or erreurs == 8


def demarrer():
    global erreurs

    print("JEU DU PENDU")
    while not boucle_pendu():
        afficher_mot()
        lettre = input("Proposez une lettre: ")
        verifier_lettre(lettre)
        afficher_pendu()

    if erreurs == 8:
        print(f'Désolé vous avez perdu, le mot était {mot}')
    else:
        print('Bravo vous avez gagné')
        print(mot)


demarrer()