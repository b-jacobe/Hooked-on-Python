"""
my_cars.py

Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.

Created: 3-11-19
@author: Brian Jacobe
"""
from restaurant import Restaurant

panda_express = Restaurant("Panda Express", "Fast-Food")
panda_express.describe_resturant()
