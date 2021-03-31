#!/usr/bin/env python3
import random

class Personne:

    def __init__(self, nom, prenom):
        self.nom    = nom
        self.prenom = prenom

    def se_presenter(self):
        print("Je suis {} {}".format(self.prenom, self.nom))

    def __repr__(self):
        print("Je suis {} {}".format(self.prenom, self.nom))

    def _get_prenom(self):
        try:
            return self.prenom
        except:
            print("Cannot get prenom")

    def _get_nom(self):
        try:
            return self.nom
        except:
            print("Cannot get nom")

    def _set_prenom(self, newPrenom):
        try:
            self.prenom = newPrenom
        except:
            print("Cannot set nom")

    def _set_nom(self, newName):
        try:
            self.nom = newName
        except:
            print("Cannot set nom")
    property(_get_nom, _set_nom)
    property(_get_prenom, _set_prenom)

class Auteur(Personne):

    def __init__(self, nom, prenom):
        self.oeuvre = []
        super().__init__(nom, prenom)

    def listerOeuvre(self):
        transition = ["Ensuite j'ai fait", "Apres ca il y a eu", "Grace a dieu j'ai écrit celui la"]
        print("Moi, {} {} j'ai fierement écrit {} livre{}, les voicis ".format(self.nom, self.prenom, len(self.oeuvre), "s" if len(self.oeuvre) > 1 else ""))
        for oeuvre in self.oeuvre:
            print("-{}\n{}".format(oeuvre.titre,transition[random.randint(0,2)]))
        print("Mais d'autres histoires sont encore a venir !")

    def ecrireLivre(self, titre):
        self.oeuvre.append(Livre(titre, self))

class Livre:

    def __init__(self, titre, auteur):
        if type(auteur) is Auteur:
            self.titre = titre
            self.auteur = auteur
        else :
            raise TypeError("Author is an Author type")

    def print(self):
        print(self.titre)

a = Personne('a', 'aaron')
a.se_presenter()

aut = Auteur('au', 'aut')
aut.ecrireLivre('Magazine IKEA')
aut.ecrireLivre('la bible')
aut.listerOeuvre()
