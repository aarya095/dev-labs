# 9-4. Number Served

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served = self.number_served + increment
        print(f"The total number of customers served are {self.number_served}.")

restaurant = Restaurant('Thai Diner','Thai')
print(f"Number of orders served is {restaurant.number_served}.")
restaurant.set_number_served(4)
print(f"Number of orders served is {restaurant.number_served}.")
restaurant.increment_number_served(2)