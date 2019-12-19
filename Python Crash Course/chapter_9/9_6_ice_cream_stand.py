"""
9_6_ice_cream_stand.py

An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.

Created: 3-7-19
@author: Brian Jacobe

"""

class Restaurant():
	"""Restaurant class that defines the basic info of a restaurant."""
	def __init__(self, resturant_name, cuisine_type):
		"""Initialize Restaurant class attributes"""
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type

	def describe_resturant(self):
		"""Returns the restaurant and it's cuisine type"""
		rest_description = self.resturant_name.title() + " is a " + self.cuisine_type + " restaurant."
		return rest_description

	def open_restaurant(self):
		"""Returns the open status of a restaurant"""
		rest_status = self.resturant_name.title() + " is open!"
		return rest_status

class IceCreamStand(Restaurant):
	""" Child class of Restaurant that serves multiple flavors of ice cream to customers """
	def __init__(self, resturant_name, cuisine_type):
		super().__init__(resturant_name, cuisine_type)
		self.flavors = ['vanilla','chocolate','strawberry','cookies n cream','caramel', 'coffee']

	def desribe_flavors(self):
		ice_cream_flavors = "The following flavors are served: "
		print(ice_cream_flavors)
		for ice_cream in self.flavors:
			print(ice_cream)
		return ""

baskin_robins = IceCreamStand('Baskin Robins', 'Ice Cream Stand')
print(baskin_robins.desribe_flavors())
