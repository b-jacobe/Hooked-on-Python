"""
7_8_deli.py

Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.

Created: 2-5-19
@author: Brian Jacobe

"""

sandwich_orders = ["chicken terriyaki", "roast beef", "spicy italian"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("Order for: " + sandwich.title() + " is complete.")
	finished_sandwiches.append(sandwich)
print("\nList of sandwich orders:")
for order in finished_sandwiches:
	print(order)
