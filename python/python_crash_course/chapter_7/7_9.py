sandwich_orders = ['Vegeterian','Pastrami','Non-Vegeterian','Grilled','Pastrami','Cheese','Club','Pastrami']

print("Deli has ran out of pastrami sandwiches.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)