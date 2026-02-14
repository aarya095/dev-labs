# 7-5. Movie Tickets

print("--Movie Theater--\n")
print("Enter 0 to exit.")
while True:
    try:
        user_input = int(input("Enter you age: "))
        if user_input == 0:
            break
        if user_input < 0:
            print("Invalid Age.")
        if user_input < 3:
            print("The movie ticket is free.")
        elif 3 <= user_input <= 12:
            print("The movie ticket cost is $10.")
        elif user_input > 12:
            print("The movie ticket cost is $15.")
    except ValueError:
        print("Invalid Input!")

