"""
9_4_number_served.py

Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.

Created: 3-2-19
@author: Brian Jacobe

"""

class Restaurant():
	def __init__(self, resturant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant"""
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_resturant(self):
		"""Describes the type of restaurant"""
		desc_restaurant = self.resturant_name.title() + " is a " + self.cuisine_type + " restaurant."
		return desc_restaurant

	def open_restaurant(self):
		"""Displays that the restaurant is open"""
		op_restaurant = self.resturant_name.title() + " is open!"
		return op_restaurant

	def set_number_served(self, service):
		"""Sets the number of customers served"""
		self.number_served = service

	def increment_number_served(self, service):
		"""Adds to the existing number of served customers"""
		self.number_served += service

new_restaurant = Restaurant('Marin Pizza', 'Italian')
print(new_restaurant.describe_resturant())
print(new_restaurant.open_restaurant())
print("Customers served: " + str(new_restaurant.number_served))
new_restaurant.number_served = 100
print("Customers served: " + str(new_restaurant.number_served))
new_restaurant.set_number_served(150)
print("Customers served: " + str(new_restaurant.number_served))
new_restaurant.increment_number_served(10)
print("Customers served: " + str(new_restaurant.number_served))
