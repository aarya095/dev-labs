# 10-8. Cats and Dogs | 10-9. Silent Cats and Dogs

try:
    with open('cats.txt') as f:
        cat_txt = f.readlines()

    print(cat_txt)

    with open('dogs.txt') as f:
        dog_txt = f.readlines()

    print(dog_txt)

except FileNotFoundError:
    #print("File not found, please ensure that the file is there.")
    pass