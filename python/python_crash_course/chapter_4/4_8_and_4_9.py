# 4-8. Cubes | 4-9. Cube Comprehension

cubes = []

for value in range(1,11):
    cube = value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

cubes = [value**3 for value in range(1,11)]
print(cubes)