"""Restaurant rating lister."""


# put your code here
import os
import sys
import random
path = ''
dirs = os.listdir(path)

restuarant_dict = {
    'restuarants' : []
}

def select_file():
    for file in dirs:
        if file.endswith('.txt'):
            print(file)
    print('Welcome to the Python Rating Program!')
    choice = input('Select a file to use or type "other" to upload a file:\n')
    if choice == 'other':
        path = input('Enter the path of the file to use:\n')
        f = open(f'{path}', 'r')
    else:
        f = open(f'{choice}', 'r')
    for line in f:
        new_line = line.split(':')
        new_line[1] = new_line[1].strip()
        restuarant_dict['restuarants'].append({'name':f'{new_line[0]}', 'rating': float(f'{new_line[1]}')})
    print(f'{choice} selected')
    print('')
    user_choices()

def user_choices():
    print('Welcome to the Restuarant Rater!')
    choice = input('''Would you like to: 
    (s) See all restuarants & ratings
    (a) Add a new restuarant
    (u) Update random restuarant's rating
    (q) Quit \n''')
    if choice == 's':
        seeRatings()
    elif choice == 'a':
        getRest()
    elif choice == 'q':
        quit()
    elif choice == 'u':
        updateRating()
    else:
        print('Must pick (s), (a), or (q)\n')
        user_choices()

def seeRatings():
    restuarant_dict['restuarants'] = sorted(restuarant_dict['restuarants'], key=lambda k: k['name'])
    print('Here are the restuarants and their ratings:\n')
    for r in restuarant_dict['restuarants']:
        print(f"{r['name']} is rated at {r['rating']}")
    print('')
    user_choices()

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
    print('Restuarant Added! \n')
    user_choices()


def updateRating():
    for r in restuarant_dict['restuarants']:
        print(r['name'])
    choice = input('What restuarant would you like to update: ')
    for n in restuarant_dict['restuarants']:
        if n['name'] == choice:
            rest = n
            print(f"{n['name']} has a rating of {n['rating']}")
            break
    new_rating = float(input('What do you want to rate it?: '))
    rest['rating'] = new_rating
    print('Success\n')
    user_choices()

select_file()