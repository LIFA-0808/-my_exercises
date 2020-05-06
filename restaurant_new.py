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


class IceCreamStand(Restaurant):
    """Creating a new Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'coconut', 'vanilla']

    def view_flavors(self):
        print('You can choose from: ' + ', '.join(self.flavors))


first_restaurant = Restaurant('Red Lobster', 'seafood')
second_restaurant = Restaurant('GanVanChi', 'chinese food')
third_restaurant = Restaurant('Broken chair', 'bar')
print(first_restaurant.restaurant_name)
print(first_restaurant.cuisine_type)
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

# 9-4
first_restaurant.get_number_served()
first_restaurant.number_served = 3
print(str(first_restaurant.number_served))
first_restaurant.set_number_served(14)
first_restaurant.get_number_served()
first_restaurant.increment_number_served(12)
first_restaurant.get_number_served()

# 9-6
ice = IceCreamStand('Movespeak', 'Ice cream')
ice.view_flavors()
