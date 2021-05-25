import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.indcareer.com/find/all-colleges-in-delhi?page=2")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

# print(soup.title)
# print(soup.title.text)

# print(soup.p.text)
# print(soup.a)
# print(soup.find_all('a')[-1].get('href'))

# for tag in soup.find_all('a'):
#     print(tag.get('href'))

# print(soup.get_text())