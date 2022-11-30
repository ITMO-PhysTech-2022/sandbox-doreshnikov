import json

with open('cities.json') as config:
    data = json.load(config)

s = input('Enter a new city: ')
data['cities'].append(s)

with open('cities.json', 'w') as config:
    json.dump(data, config, indent=2)
