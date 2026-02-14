# 9-1. Restaurant | 

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("The restaurant is open.")

my_restaurant = Restaurant("Nura","Mexican")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()