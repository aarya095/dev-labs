import json

user_input = input("Enter your favorite number: ")

with open('fav_num.json', 'w') as f:
    json.dump(user_input, f)

