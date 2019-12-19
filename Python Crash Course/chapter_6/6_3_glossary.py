"""
6_3_favorite_numbers.py

Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
6-3. Glossary: A Python dictionary can be used to model

Created: 1-25-19
@author: Brian Jacobe

"""

glossary = {
	"Method":"An action that is used to perform on a piece of data.",
	"List":"A collection of items in a particular order.",
	"Dictionary":"A collection of key-value pairs.",
	"Tuple": "Immutable list, defined with parentheses instead of brakets.",
	"If-Elif-Else":"Examines the current state of a program and responds appropriately to that state."
	}

for k, v in glossary.items():
	print("\nTerm: " + k)
	print("Description: " + str(v))