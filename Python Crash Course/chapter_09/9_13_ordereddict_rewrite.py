"""
9_13_ordereddict_rewrite.py

Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.

Created: 3-22-19
@author: Brian Jacobe
"""
from collections import OrderedDict

glossary = OrderedDict()


glossary = {
	"Method":"An action that is used to perform on a piece of data.",
	"List":"A collection of items in a particular order.",
	"Dictionary":"A collection of key-value pairs.",
	"Tuple": "Immutable list, defined with parentheses instead of brakets.",
	"If-Elif-Else":"Examines the current state of a program and responds appropriately to that state.",
	"Set" : "Identifies unique values within a list.",
	"Sorted" : "Sorts a alpha-numeric list.",
	"Del" : "Permanently deletes a value.",
	"Range" : "Generate a series of numbers",
	"For Loop" : "Ability to loop through a list given a declared variable"
	}

for k, v in glossary.items():
	print("\nTerm: " + k)
	print("Description: " + str(v))