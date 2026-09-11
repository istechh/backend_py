"""
Importe requests
Fait une requête GET vers cette API publique et gratuite de test : https://api.github.com
Affiche le code de statut de la réponse (200 = succès)
Affiche le contenu de la réponse, converti en dictionnaire Python (avec .json(), une méthode intégrée directement à la réponse de requests !)




"""


import requests

url = "https://api.github.com"

req = requests.get(url)

print(req.status_code)

data = req.json()

print(data)
