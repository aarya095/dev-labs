with open('learning_python.txt') as f:
    contents = f.read()

for i in range(0,3):
    print(contents)
    print()

# Storing contents of the .txt file in a list
with open('learning_python.txt') as f:
    contents = f.readlines()

for i in range(0,3):
    print(contents)
    print()