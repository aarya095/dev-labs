import json

filename = 'username.json'

def get_and_store_usrname():

    username_input = input("Enter your name: ")
    with open(filename, 'w') as f:
        json.dump(username_input, f)
    print(f"We'll remember you {username_input.title()}.")

def greet_user():

    with open(filename) as f:
        username = json.load(f)

    user_input = input(f"Is your username {username} correct? Enter yes or no. ").lower().strip()
    if user_input == 'no':
        get_and_store_usrname()
    elif user_input == 'yes':
        print(f"Hello {username.title()}!")
    else:
        print("Invalid Input! Enter yes or no.")

if __name__ == '__main__':
    greet_user()