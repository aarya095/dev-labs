favorite_numbers = {
    'roger': [65, 23, 34],
    'wanda' : [2,50,23,321],
    'Thor' : [102,92,1002],
    'Peter' : [987, 988, 999],
    'drax' : [6,10,100,1000]
}

for person, favorite_number in favorite_numbers.items():

    print(f"{person.title()}'s favorite numbers are ", end='')
    print(*favorite_number, sep=', ',end='')
    print('.')
