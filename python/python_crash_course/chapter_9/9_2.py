# 9-2. Three Restaurants

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' has {self.cuisine_type} cuisine.")

restaurant_1 = Restaurant('Thai Diner','Thai')
restaurant_2 = Restaurant('Zou Zou','Greek')
restaurant_3 = Restaurant('Lilia','Italian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()