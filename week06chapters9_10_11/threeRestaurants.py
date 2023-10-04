# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
        

restaurant1 = Restaurant('KFC', 'chicken')
print(restaurant1.name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Ginza', 'asian')
print(restaurant2.name)
print(restaurant2.cuisine_type)

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('Mochis', 'asian')
print(restaurant3.name)
print(restaurant3.cuisine_type)

restaurant3.describe_restaurant()
restaurant3.open_restaurant()
