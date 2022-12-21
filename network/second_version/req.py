import requests

# method = GET / POST / ...
response = requests.get(
    'https://github.com/doreshnikov',
    params={'tab': 'repositories'},
    # https://github.com/doreshnikov?tab=repositories
)

print(response.status_code)
# for k, v in response.headers.items():
#     print(k, v)

with open('github.html', 'w', encoding='utf-8') as out:
    out.write(response.text)

import bs4  # beautifulsoup4

html = response.text
source = bs4.BeautifulSoup(html)
element = source.find('div', {'id': 'user-repositories-list'})
with open('html+bs', 'w') as f:
    for item in element.find_all('a', {'itemprop': 'name codeRepository'}):
        print(item.text.strip(), file=f)

# API

response = requests.get('https://api.github.com/users/doreshnikov/repos?per_page=50')
data = response.json()
with open('api+json', 'w') as f:
    for item in data:
        print(item['name'], file=f)
