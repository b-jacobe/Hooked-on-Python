"""
7_9_no_pastrami.py

Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.

Created: 2-5-19
@author: Brian Jacobe

"""

sandwich_orders = ["chicken terriyaki","pastrami", "roast beef","pastrami", "spicy italian", "pastrami"]

print("We have run out of pastrami. We apologize for the inconvenience.\n")

while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
	print(sandwich)