# 9-6. Ice Cream Stand

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, ice_falvour):
        super().__init__(restaurant_name, cuisine_type)
        self.ice_falvour = ice_falvour

    def display_flavour(self):
        print(f"We have {self.ice_falvour}.")

myIceCreamStand = IceCreamStand("The RobinHood","English","Butterscotch")
myIceCreamStand.display_flavour()