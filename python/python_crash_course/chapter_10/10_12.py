import json

user_input = input("Enter your favorite number: ")

with open('fav_num.json', 'w') as f:
    json.dump(user_input, f)

with open('fav_num.json') as f:
    data = json.load(f)

print(f"I know yout favourite number! Its {data}.")