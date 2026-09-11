"""

Écris un programme qui :

Définit une classe Chien avec un attribut nom
Crée un objet (une "instance") de cette classe, avec le nom "Rex"
Affiche le nom de ce chien








"""

class Chien:
    def __init__(self,nom:str):
        self.nom=nom

    def afficher(self):
    
        print(f'le nom de ce chien est {self.nom}')


chien_1=Chien("Rex")
chien_1.afficher()

class BergerAllemand(Chien):

    def __init__(self,nom,age):
        super().__init__(nom)
        self.age=age

    def afficher_chien(self):
        print(f"le chien{self.nom} a {self.age} ans")

chien_b=BergerAllemand("Dex",3)
chien_b.afficher_chien()




"""
Écris un programme qui :

Définit une classe CompteBancaire avec :
un attribut solde, initialisé à 0 par défaut à la création (pas besoin de le passer en paramètre)
une méthode deposer(montant) qui ajoute montant au solde
une méthode afficher_solde() qui affiche le solde actuel, sous la forme : "Solde : 150"
Crée un compte, dépose 100, puis dépose encore 50
Affiche le solde final


"""



class CompteBancaire:
    
    def __init__(self):
        self.solde=0
    def deposer_montant(self,montant):
        self.solde+=montant


    def afficher_solde(self):
    
        print(f"le solde est, Solde:{self.solde}")

Compte=CompteBancaire()
Compte.deposer_montant(5999)
Compte.deposer_montant(74775)
Compte.afficher_solde()







'''
cris un programme qui :

Définit une classe Rectangle avec deux attributs : largeur et hauteur (passés en paramètres à la création)
Ajoute une méthode calculer_aire() qui retourne (avec return, pas print) le résultat de largeur * hauteur
Crée un rectangle avec largeur = 5 et hauteur = 3
Affiche le résultat de calculer_aire()









'''


class Rectangle:
    def __init__(self,longeur,largeur):
        self.longeur=longeur
        self.largeur=largeur

    def aire(self):
        aire_rectangle=self.longeur*self.largeur
        return aire_rectangle



rec=Rectangle(12,12)
print(rec.aire())
