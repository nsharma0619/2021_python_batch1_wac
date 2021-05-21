import requests

endpoint = "https://v2.jokeapi.dev/joke/Programming"

response = requests.get(endpoint)

data = response.json()
print(data['category'])