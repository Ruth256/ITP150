# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    """A model/blueprint of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        description = self.restaurant_name + " serves " + self.cuisine_type + " cuisine."
        print(f"{description}")

    def open_restaurant(self):
        """Is it open?"""
        openStatus = self.restaurant_name + " is open."
        print(f"{openStatus}")

restaurant1 = Restaurant('Twins', 'pizza')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()