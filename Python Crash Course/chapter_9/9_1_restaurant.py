"""
9_1_restaurant.py

Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

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

print(panda_restaurant.describe_resturant())
print(panda_restaurant.open_restaurant())
