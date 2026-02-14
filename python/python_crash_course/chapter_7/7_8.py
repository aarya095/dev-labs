sandwich_orders = ['Vegeterian','Non-Vegeterian','Grilled','Cheese','Club']

finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

print("\nI have made the following sandwiches ",end='')
print(*finished_sandwiches, sep=', ')