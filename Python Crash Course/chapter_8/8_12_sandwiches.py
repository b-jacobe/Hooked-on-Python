"""
8_12_sandwiches.py

Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.

Created: 2-14-19
@author: Brian Jacobe

"""

def customer_order(bread, cheese, meat, *veggies):
	print("\nThe customer ordered the following:\n")
	print(bread + "\n" + cheese + "\n" + meat)
	for veg in veggies:
		print(veg)
	return 0

veg = ["Spinach", "Onions", "Pickles", "Tomatoes"]
print(customer_order('Wheat', 'Pepper Jack', 'Tuna', veg))
