favorite_numbers = {
    'roger': 65,
    'wanda' : 2,
    'Thor' : 102,
    'Peter' : 987,
    'drax' : 6
}

for key, value in favorite_numbers.items():
    print(f"{key.title()}'s faorite number is '{value}'.")

for name in favorite_numbers.keys():
    print(name.lower())

for number in favorite_numbers.values():
    print(number)

for value in favorite_numbers:
    print(value)

"""print(f"Roger's favorite number is {favorite_numbers['roger']}.")
print(f"Wanda's favorite number is {favorite_numbers['wanda']}.")
print(f"Thor's favorite number is {favorite_numbers['Thor']}.")
print(f"Peter's favorite number is {favorite_numbers['Peter']}.")
print(f"Drax's favorite number is {favorite_numbers['drax']}.")"""