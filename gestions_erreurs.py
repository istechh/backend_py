"""
Demande deux nombres à l'utilisateur (converti avec int())
Essaie de diviser le premier par le second
Si tout se passe bien, affiche le résultat
Si l'utilisateur tape 0 comme deuxième nombre (division par zéro, impossible mathématiquement), affiche "Erreur : division par zéro impossible." au lieu de faire planter le programme






"""




nombre_1=int(input("donne le premier nombre : "))

nombre_2=int(input("donne le deuxieme nombre : "))

try:
    resultat=nombre_1/nombre_2
    print(resultat)

except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")

try:
    age = int(input("Quel est ton age ? "))

    if age >= 18:
        print("Tu es majeur.")
    else:
        print("Tu es mineur.")

except ValueError:
    print("Valeur invalide.")