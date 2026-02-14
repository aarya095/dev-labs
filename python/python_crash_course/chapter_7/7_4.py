# 7-4. Pizza Toppings

while True:
    user_input = input("Enter a pizza topping: ").lower().strip()
    if user_input == 'quit':
        break
    print(f"I'll add {user_input.title()} to your pizza.")