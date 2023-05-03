import requests

amount = 10
type = "boolean"

parameters = {  # Parametros de la pagina que mientras mas info o cosas pidamos mas parametros nos aparecen.
    "amount": amount,
    "type": type,
    "category": 18,
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=18", params=parameters)
response.raise_for_status()
data = response.json()

print(data)

question_data = data["results"]

