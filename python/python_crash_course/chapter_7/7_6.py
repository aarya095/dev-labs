# 7-6. Three Exits

user_input = ''

while user_input != 'quit':
    user_input = input("Enter a pizza topping: ").lower().strip()
    print(f"I'll add {user_input.title()} to your pizza.")