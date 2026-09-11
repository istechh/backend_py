response="Bonjour, je code en Python !"

print(response)


'''
Objectif : Créer des variables numériques et faire une opération simple.

Consigne :
Écris un programme qui :

Crée une variable contenant le nombre 8
Crée une autre variable contenant le nombre 3
Additionne les deux et affiche le résultat

Exemple de résultat attendu (sortie du programme) :

11

Indices :

Pour stocker un nombre, pas besoin de guillemets (contrairement au texte) : age = 25 par exemple.
Le symbole + sert à additionner deux nombres.
Tu peux soit calculer le résultat dans une troisième variable, soit faire l'addition directement à l'intérieur de print().





Objectif : Découvrir la fonction input() pour récupérer une information tapée par l'utilisateur, et l'afficher.

Consigne :
Écris un programme qui :

Demande à l'utilisateur de saisir son prénom (avec un message du type "Quel est ton prénom ?")
Stocke ce qu'il tape dans une variable
Affiche un message de bienvenue personnalisé
Objectif : Combiner input() et calcul, en convertissant du texte en nombre.

Consigne :
Écris un programme qui :

Demande à l'utilisateur son âge actuel
Calcule et affiche quel âge il aura dans 10 ans

Exemple d'exécution attendue :

Quel est ton âge ? 25
Dans 10 ans, tu auras 35 ans.


'''
nombre=8
nombre_1=3

addition=nombre+nombre_1

print(f"{addition}")


saisie=input("Quel est ton prenom?")

print(f"Bienvenue, {saisie} bientot tu seras expert en python et en machine learning!")



age=int(input("Quel est ton age ? "))
age_futur=age+10

print(f"Dans 10 ans, tu auras {age_futur} ans !")


"""

Consigne :
Écris un programme qui :

Demande l'âge de l'utilisateur
Affiche "Tu es majeur." si l'âge est supérieur ou égal à 18
Affiche "Tu es mineur." sinon

Objectif : Utiliser l'opérateur modulo % combiné à une condition.

Consigne :
Écris un programme qui :

Demande un nombre entier à l'utilisateur
Affiche "Ce nombre est pair." si le nombre est pair
Affiche "Ce nombre est impair." sinon



"""


try:
    age = int(input("Quel est ton age ? "))

    if age >= 18:
        print("Tu es majeur.")
    else:
        print("Tu es mineur.")

except ValueError:
    print("Valeur invalide.")



nombre=int(input("donne un nombre entier "))

if nombre%2==0:
    print("Ce nombre est pair.")
else:
    print("Ce nombre est impair.")




