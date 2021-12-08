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
    restuarant_dict['restuarants'].append({'name':f'{new_line[0]}', 'rating': float(f'{new_line[1]}')})

def getRest():
    name = input('Enter the restuarant name: ').capitalize()
    rating = (input('Enter your rating for the restuarant: '))
    if is_input(rating) == True:
        rating = float(rating)
        createRest(name, rating)
    else:
        print('Must rate 1-5')
        getRest()

def is_input(rating):
    try:
        float(rating)
        rating = float(rating)
        if rating >= 1 and rating <= 5:
            return True
    except ValueError:
        return False

def createRest(name, rating):
    restuarant_dict['restuarants'].append({'name':f'{name}', 'rating': f'{rating}'})

new_rest = input('Have a restuarant to add? (y/n) ')

if new_rest == 'y':
    getRest()

restuarant_dict['restuarants'] = sorted(restuarant_dict['restuarants'], key=lambda k: k['name'])

print('Here are the restuarants and their ratings:\n')
for r in restuarant_dict['restuarants']:
    print(f"{r['name']} is rated at {r['rating']}")
