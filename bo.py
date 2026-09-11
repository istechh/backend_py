'''
Objectif : Découvrir la boucle for pour répéter une action automatiquement.

Consigne :
Écris un programme qui affiche les nombres de 1 à 5, chacun sur une ligne différente.

Exemple de résultat attendu (sortie du programme) :

1
2
3
4
5

Objectif : Combiner boucle for, calcul, et f-string.

Consigne :
Écris un programme qui :

Demande à l'utilisateur un nombre (ex: 7)
Affiche sa table de multiplication de 1 à 10

Objectif : Découvrir la boucle while, qui répète tant qu'une condition est vraie (contrairement à for qui répète un nombre de fois défini à l'avance).

Consigne :
Écris un programme qui affiche un compte à rebours de 5 à 1, puis affiche "Décollage !" à la fin.

Objectif : Renforcer la boucle while avec une condition qui dépend d'une comparaison (pas juste d'un compteur qui monte ou descend).

Consigne :
Écris un programme qui :

Définit un nombre secret dans une variable, par exemple nombre_secret = 7
Demande à l'utilisateur de deviner ce nombre, encore et encore, tant qu'il ne trouve pas la bonne réponse
Dès que l'utilisateur trouve le bon nombre, affiche "Bravo, tu as trouvé !"








'''


for i in range(1,6):
    print(i)

nombre = int(input("Donne-moi un nombre : "))

for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")

i=5
while i>0:
    print(i)
    i=i-1
print("Décollage !")



nombre_secret=7

i=int(input("donne moi le nombre secret : "))

while  i==7:
   

    print("Bravo, tu as trouvé !")
    i=i+1