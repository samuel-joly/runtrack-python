#!/usr/bin/env python3

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
