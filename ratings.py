"""Restaurant rating lister."""


# put your code here
from os import read

f = open('scores.txt', 'r')

restuarant_dict = {
    'restuarants' : []
}

for line in f:
    new_line = line.split(':')
    new_line[1] = new_line[1].strip()
    restuarant_dict['restuarants'].append({'name':f'{new_line[0]}', 'rating': f'{new_line[1]}'})

new_rest = input('Have a restuarant to add? (y/n) ')

if new_rest == 'y':
    rest_name = input('Enter the restuarant name: ')
    rest_rating = input('Enter your rating for the restuarant: ')
    restuarant_dict['restuarants'].append({'name':f'{rest_name}', 'rating': f'{rest_rating}'})
else:
    print('Here are the restuarants and their ratings:\n')

restuarant_dict['restuarants'] = sorted(restuarant_dict['restuarants'], key=lambda k: k['name'])

for r in restuarant_dict['restuarants']:
    print(f"{r['name']} is rated at {r['rating']}")