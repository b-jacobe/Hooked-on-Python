"""
8_9_magicians.py

Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.

Created: 2-11-19
@author: Brian Jacobe
Updated: 12-28-19

"""

def show_magicians(magician):
  result = list()
  for mage in magician:
	  result.append(mage.title())
  return result

magician_names = ["Harry", "Gandalf", "Yen Sid"]

print(show_magicians(magician_names))
