import json

with open('fav_num.json') as f:
    data = json.load(f)

print(f"I know yout favourite number! Its {data}.")