'''
Ma liste de courses

Objectif : Créer une liste, y ajouter des éléments, et l'afficher.

Consigne :
Écris un programme qui :

Crée une liste vide appelée courses
Ajoute les éléments "pommes", "pain", et "lait" à cette liste, un par un
Affiche la liste complète







Écris un programme qui :

Crée une liste de nombres : nombres = [4, 8, 15, 16, 23]
Calcule la somme de tous ces nombres à l'aide d'une boucle for
Affiche le résultat final





'''



courses=[]

courses.append("pomme")
courses.append("pain")
courses.append("lait")

print(courses)



total=0
nombres = [4, 8, 15, 16, 23]

for i in nombres:
    total=total+i
print(total)
