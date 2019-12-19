"""
6_4_glossary_2.py

Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

Created: 1-26-19
@author: Brian Jacobe

"""

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