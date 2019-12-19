"""
8_4_large_t_shirts.py

Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

Created: 2-10-19
@author: Brian Jacobe

"""

def make_shirt(size="large", message="I love Python"):
	print("Shirt Size: " + size)
	print("Shirt Message: " + message + "\n")

make_shirt()
make_shirt("medium")