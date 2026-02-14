favorite_places = {
    'Akaash' : ['Machu Pichu','Mount Everest'],
    'Reshma' : ['Taj Mahal','Jagannath Mandir','Surya Mandir'],
    'Namrata' : ['Lakshwadeep','Singapore']
}

for name, places in favorite_places.items():

    print(f"{name.title()}'s places are ", end='')
    print(*places, sep=', ', end='')
    print('.')