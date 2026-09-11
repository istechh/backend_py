"""
Crée (ou ouvre) un fichier appelé message.txt
Écrit dedans le texte "Bonjour depuis Python !"
Ferme proprement le fichier






"""


with open("message.txt","w") as f:
    contenu=f.write("Bonjour depuis python!")
    print(contenu)



with open("message.txt","r") as f:
    cont=f.read()
    print(cont)