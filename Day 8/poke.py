import requests
pokemon_name = input("Enter pokemon name: ")
url = f"https://api.pokemontcg.io/v1/cards?name={pokemon_name}"

response = requests.get(url)
data = response.json()

img_url = data['cards'][3]["imageUrl"]
img_response = requests.get(img_url)

with open("./poke.png", 'wb') as f:
    for item in img_response.iter_content(4096):
        f.write(item)



import matplotlib.pyplot as plt

data = plt.imread("./poke.png")
plt.imshow(data)
plt.show()