try:
    user_input1 = int(input("Enter num1: "))
    user_input2 = int(input("Enter num2: "))
except ValueError:
    print("Enter an integer!")

else:
    print(f"Sum of two numbers is {user_input1+user_input2}.")