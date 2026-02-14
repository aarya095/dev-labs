while True:
    try:
        user_input = int(input("Enter a number: "))

        if (user_input % 10) == 0:
            print(f"{user_input} is a multiple of 10.")
            break
    except ValueError:
        print("Please enter an integer")