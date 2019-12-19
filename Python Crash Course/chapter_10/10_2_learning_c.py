"""
10_2_learning_c.py

You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:

>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'

Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.

Created: 3-26-19
@author: Brian Jacobe
"""

filename = "learning_python.txt"

with open(filename) as file_object:
	language = file_object.read()

print("===== Python ====")
print(language)

print("===== C ====")
print(language.replace('Python', 'C'))
