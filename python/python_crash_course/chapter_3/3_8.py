# 3-8. Seeing the World:

places_to_visit = ['macu pichu','mount everest','mount fuji','pyramids','moscow']

print(places_to_visit)

print("\nTemporaryily stored list:")
print(sorted(places_to_visit))

print("\nHere is the original list:")
print(places_to_visit)

print("\nTemporaryily stored list but in reverse aplhabetical order:")
print(sorted(places_to_visit, reverse=True))

print("\nHere is the original list:")
print(places_to_visit)

places_to_visit.reverse()
print("\nReversed list:")
print(places_to_visit)

places_to_visit.reverse()
print("\nAgain Reversed list:")
print(places_to_visit)

places_to_visit.sort()
print("\Alphabetically sorted list:")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nnReverse Alphabetically sorted list:")
print(places_to_visit)