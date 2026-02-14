# 3-10. Every Function | 3-11. Intentional Error

cities = ['delhi','moscow','new york','las vegas','mumbai']

print(cities)

print(cities[3])

print(cities[-1])

cities[2]='Chennai'
print(cities)

cities.append('petersburg')
print(cities)

cities.insert(4,'paris')
print(cities)

del cities[3]
print(cities)

popped_city = cities.pop()
print(cities)
print(popped_city)

cities.remove('delhi')
print(cities)

print("\nHere is the sorted list:")
print(sorted(cities))

print("\nHere is the original list again:")
print(cities)

cities.reverse()
print('\nReversed list:',cities)

print(len(cities))

# print(cities[21])