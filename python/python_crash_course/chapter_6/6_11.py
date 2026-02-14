cities = {

    'mumbai' : {
        'country' : 'india',
        'population' : '21.7 million',
        'fact' : 'Mumbai is the most populous city in India'
    },

    'st. petersburg' : {
        'country' : 'russia',
        'population' : '5.598 million',
        'fact' : "The world's northernmost major metropolis"
    },

    'minsk' : {
        'country' : 'belarus',
        'population' : '9 million',
        'fact' : 'Around 40 percent of Belarus is covered by forest'
    }
}

for city, city_info in cities.items():

    print(f"{city.title()} is in {city_info['country'].title()}.")
    print(f"The polulation of {city.title()} is {city_info['population'].title()}.")
    print(f"""A fact about {city.title()} is "{city_info['fact'].title()}".""")
    print()