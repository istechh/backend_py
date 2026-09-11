"""

Importe le module json
Crée un dictionnaire utilisateur avec les clés "nom" ("Alice"), "age" (28), "ville" ("Lyon")
Convertit ce dictionnaire en texte JSON avec json.dumps(), et affiche le résultat
Convertit ce texte JSON à nouveau en dictionnaire Python avec json.loads(), et affiche le résultat
"""

import json

utilisateur = {
    "nom": "Alice",
    "age": 28,
    "ville": "Lyon"
}

texte_json = json.dumps(utilisateur)

print(texte_json)

utilisateur_python = json.loads(texte_json)

print(utilisateur_python)