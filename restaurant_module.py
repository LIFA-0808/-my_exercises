"""Example for importing"""


class Restaurant:
    """Creating a new restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def get_number_served(self):
        return print('Today we have ' + str(self.number_served) + ' guests!')

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, guests):
        self.number_served += guests

    def describe_restaurant(self):
        return print(self.restaurant_name.title() + ': ' + self.cuisine_type.lower())

    def open_restaurant(self):
        return print(self.restaurant_name.title() + ', We are open now!')
