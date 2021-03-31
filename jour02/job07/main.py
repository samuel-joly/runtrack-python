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
        print("Moi, {} {} j'ai fierement écrit {} livre{}, les voicis ".format(self.nom, self.prenom, len(self.oeuvre), "s" if len(self.oeuvre) > 1 else ""))
        for oeuvre in self.oeuvre:
            print("-{}".format(oeuvre.titre))
        print("Mais d'autres histoires sont encore a venir !")

    def ecrireLivre(self, titre):
        self.oeuvre.append(Livre(titre, self))


class Client(Personne):
    def __init__(self, nom, prenom):
        self.collection = []
        super().__init__(nom, prenom)

    def inventaire(self):
        print("Moi, {} {} j'ai fierement loué {} livre{}, les voicis ".format(self.nom, self.prenom, len(self.collection), "s" if len(self.collection) > 1 else ""))
        for oeuvre in self.collection:
            print("-{}\n".format(oeuvre))
        print("Mais j'ai toujours plus faim d'histoires")


class Livre:

    def __init__(self, titre, auteur):
        if type(auteur) is Auteur:
            self.titre = titre
            self.auteur = auteur
        else :
            raise TypeError("Author is an Author type")

    def print(self):
        print("Titre:{} Auteur:{}".format(self.titre, self.auteur))

class Bibliotheque:

    def __init__(self, nom, catalogue=[]):
        self.nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, autor, livre_titre, quantite):
        for livre in autor.oeuvre:
            if livre.titre == livre_titre:
                self.catalogue[livre_titre] = quantite
                return
        print("Pas de {} dans la biblio de {} {} !".format(livre_titre, autor.nom, autor.prenom))

    def inventaire(self):
        print("Nous avons {} livre{}, les voicis ".format(len(self.catalogue), "s" if len(self.catalogue) > 1 else ""))
        for livre in self.catalogue:
            print("{} {} en {} exemplaire{}".format(livre, self.catalogue[livre],len(self.catalogue), "s" if len(self.catalogue)>1 else ""))

    def louerLivre(self, client, nom_livre):
        if nom_livre in self.catalogue :
            self.catalogue[nom_livre] -= 1
            client.collection.append(nom_livre)
        else :
            print("Pas de ca dans notre biblio !")

    def rendreLivre(self, client, livre):
        if livre in client.collection:
            for i in range(len(client.collection)):
                if client.collection[i] == livre:
                    del client.collection[i]
                    break
            self.catalogue[livre] += 1
        else :
            print("Le client {} {} n'as pas le livre {}".format(client.nom, client.prenom, livre))

a = Personne('a', 'aaron')
#a.se_presenter()

aut = Auteur('au', 'aut')
aut.ecrireLivre('Magazine IKEA')
aut.ecrireLivre('la bible')
#aut.listerOeuvre()

cli = Client('cli', 'Client')
cli.inventaire()

bi = Bibliotheque('sacre coeur', {})
bi.louerLivre(cli, 'Magazine IKEA')
bi.acheterLivre(aut, 'Magazine IKEA', 4)
bi.inventaire()
bi.louerLivre(cli, 'Magazine IKEA')
cli.inventaire()
bi.inventaire()
bi.rendreLivre(cli, 'Magazine IKEA')

bi.inventaire()
cli.inventaire()
