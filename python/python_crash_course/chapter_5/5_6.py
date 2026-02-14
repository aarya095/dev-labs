# 5-6. Stages of Life

age = 0

if age < 0:
    print("Invalid age. Please input a valid age.")

elif age < 2:
    print("The person is a baby.")

elif 2 <= age < 4:
    print("The person is a toddler.")

elif 4 <= age < 13:
    print("The person is a kid.")

elif 13 <= age < 20:
    print("The person is a teenager.")

elif 20 <= age < 65:
    print("The person is a adult.")

elif age >= 65:
    print("The person is a elder.")
