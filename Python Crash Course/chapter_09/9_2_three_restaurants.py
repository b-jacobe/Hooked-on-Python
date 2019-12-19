"""
9_2_three_restaurants.py

Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

Created: 2-18-19
@author: Brian Jacobe

"""

class Restaurant():
	def __init__(self, resturant_name, cuisine_type):
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type

	def describe_resturant(self):
		print(self.resturant_name.title() + " is a " + self.cuisine_type + " restaurant.")
		return ""

	def open_restaurant(self):
		print(self.resturant_name.title() + " is open!")
		return ""

panda_restaurant = Restaurant("Panda Express", "Fast Food")
harmony_restaurant = Restaurant("Harmony", "Asian Cuisine")
yard_house_restaurant = Restaurant("Yard House", "New American")
print(panda_restaurant.describe_resturant())
print(harmony_restaurant.describe_resturant())
print(yard_house_restaurant.describe_resturant())