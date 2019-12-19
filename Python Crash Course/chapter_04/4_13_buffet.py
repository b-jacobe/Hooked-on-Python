"""
4_13_buffet.py

A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.

Created: 1-15-19
Last Updated: 
@author: Brian Jacobe

"""

restaurant_food = ('fries', 'salad', 'burger', 'salmon', 'veggie burger', 'milk shake')

for i in restaurant_food:
	print(i)

# Cannot modify tuple
# restaurant_food[0] = "onion rings"

restaurant_food = ('fries', 'onion rings', 'burger', 'salmon', 'veggie burger', 'cake')

for j in restaurant_food:
	print(j)