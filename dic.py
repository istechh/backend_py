"""
Écris un programme qui :

Crée un dictionnaire appelé personne contenant :
une clé "nom" avec la valeur "Dupont"
une clé "age" avec la valeur 30
une clé "ville" avec la valeur "Paris"
Affiche uniquement la valeur associée à la clé "nom"
Affiche uniquement la valeur associée à la clé "age"


"""

personne = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris"
}

for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")




"""

Écris un programme qui :

Demande l'âge de l'utilisateur
Demande s'il a un billet valide (réponse "oui" ou "non")
Affiche "Accès autorisé." si la personne a au moins 18 ans ET a répondu "oui" pour le billet
Affiche "Accès refusé." dans tous les autres cas


Écris un programme qui :

Demande le jour de la semaine (en texte, ex: "samedi")
Affiche "C'est le week-end !" si le jour est "samedi" OU "dimanche"
Affiche "C'est un jour de semaine." sinon




"""


age=int(input("donne moi ton age : "))
billet = input("As-tu un billet ? (yes/no) : ")

if (age>=18 and billet== "yes") :
    print("Accès autorisé.")
else:
    print("Accès refusé.")



jour=input("donne moi le jour de la semaine : ")
if (jour=="samedi" or jour=="dimanche"):
    print("C'est le week-end !")
else:
    print("C'est un jour de semaine.")