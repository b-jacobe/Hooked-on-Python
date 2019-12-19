"""
8_3_t_shirt.py

Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

Created: 2-10-19
@author: Brian Jacobe

"""

def make_shirt(size, message):
	print("Shirt Size: " + size)
	print("Shirt Message: " + message + "\n")

# Positional Argument
make_shirt("small","Team Liquid")

# Keyword Argument
make_shirt(size="small", message="Team Liquid")