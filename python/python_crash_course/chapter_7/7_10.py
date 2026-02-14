polling = True


while polling:
    user_input = input("What is your dream vacation?\nAns: ").lower().strip()
    if user_input == 'quit':
        break
    print(f"The user would to go to {user_input.title()}.\n")