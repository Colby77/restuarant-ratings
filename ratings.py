"""Restaurant rating lister."""


# put your code here
f = open('scores.txt', 'r')

restuarant_dict = {
    'restuarants' : []
}

for line in f:
    new_line = line.split(':')
    # print(new_line)
    new_line[1] = new_line[1].strip()
    # print(new_line)
    # new_line = line.split(':')
    # print(new_line)
    restuarant_dict['restuarants'].append({'name':f'{new_line[0]}', 'rating': f'{new_line[1]}'})
    # print(new_line)


for r in restuarant_dict['restuarants']:
    print(r.items())

# x = restuarant_dict['restuarants'].items()
# print(x)
# print(restuarants)
# print(f.read())