import requests


response = requests.get("https://currencyapi.net/api/v1/rates?key={YOU SHOULD USE YOUR KEY}&base=USD")


# print(dir(response))
# print(type(response.json()))
# print(type(response.text))

data = response.json()
rates = data["rates"]

print(f'1 USD is equal to {rates["INR"]} INR')
