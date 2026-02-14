rivers_dict = {'nile' : 'eygpt', 'ganga' : 'bharat', 'volga' : 'russia'}

for river, country in rivers_dict.items():
    print(f"River {river.title()} runs through {country.title()}.")

print()

for river in rivers_dict.keys():
    print(river)

print()

for country in rivers_dict.values():
    print(country)