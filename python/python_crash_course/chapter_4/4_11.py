# 4-11. My Pizzas, Your Pizzas

my_pizzas = ['sicilian','italian','greek']

friend_pizzas = my_pizzas[:]

my_pizzas.append('Hawaiian')
friend_pizzas.append('pepperoni')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
