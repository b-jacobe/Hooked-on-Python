"""
10_1_learning_python.py

Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.

Created: 3-26-19
@author: Brian Jacobe
"""

filename = 'learning_python.txt'

"""REPEAT 1"""
with open(filename) as file_objects:
	lines = file_objects.readlines()
	print(lines)

"""REPEAT 2"""
python_string = ""
for line in lines:
	python_string += line.rstrip()

print(python_string)

"""REPEAT 3"""
python_list = []
for line in lines:
	python_list.append(line)

print(python_list)