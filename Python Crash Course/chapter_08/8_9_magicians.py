"""
8_9_magicians.py

Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.

Created: 2-11-19
@author: Brian Jacobe

"""

def show_magicians(magician):
	for mage in magician:
		message = mage.title()
		print(message)

magician_names = ["Harry", "Gandalf", "Yen Sid"]

print(show_magicians(magician_names))
