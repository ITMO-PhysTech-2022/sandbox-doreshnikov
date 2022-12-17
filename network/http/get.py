import requests
import bs4  # beautifulsoup

response = requests.get('https://wikipedia.org')
parser = bs4.BeautifulSoup(response.text)
for elem in parser.button:
    print(elem)

response = requests.get('https://api.github.com/users/doreshnikov')
print(response.json()['created_at'])
