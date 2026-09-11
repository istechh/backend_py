'''
Découvrir la structure def pour créer une fonction.

Consigne :
Écris un programme qui :

Définit une fonction appelée dire_bonjour qui affiche "Bonjour tout le monde !"
Appelle cette fonction (c'est-à-dire, exécute-la) une fois

Exemple de résultat attendu (sortie du programme) :

Bonjour tout le monde !
Écris un programme qui :

Définit une fonction saluer qui prend un paramètre prenom
Cette fonction affiche "Bonjour, [prenom] !" (en remplaçant [prenom] par la valeur reçue)
Appelle cette fonction avec le prénom "Marie", puis une deuxième fois avec "Thomas"






'''



def dire_bonjour():
    print("Bonjour tout le monde !")




dire_bonjour()


def saluer(prenom):
    salutations=f"Bonjour {prenom}"
    return salutations


print(saluer("Marie !"))
print(saluer("Thomas !"))