while True:
    try:
        user_input1 = int(input("Enter num1: "))
        user_input2 = int(input("Enter num2: "))
        break
    except ValueError:
        print("Enter an integer!")

print(f"Sum of two numbers is {user_input1+user_input2}.")