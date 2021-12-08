"""Restaurant rating lister."""


# put your code here
f = open('scores.txt', 'r')

restuarants = []

for line in f:
    new_line = line.split(':')
    restuarants.append({'name':f'{new_line[0]}', 'rating': f'{new_line[1]}'})
    # for word in new_line:
    #     word = word.replace('\n', '2')
    # print(new_line)

for r in restuarants:
    # print(f'{r['name']}', f'{r['rating']}', sep=':')
    print(r['name'] + ':' + r['rating'])

# x = restuarants.items()
# print(x)
# print(restuarants)
# print(f.read())