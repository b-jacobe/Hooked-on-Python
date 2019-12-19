"""
write_message.py

Write into an empty text file.

Created: 3-26-19
@author: Brian Jacobe
"""

filename = "programming.txt"

outfile = open(filename, 'w')
outfile.write("Let's work on our foundations in Python. \n")
outfile.write("Study 'Python Crash Course', 'Learning Python', 'Fluent Python' and Udemy courses.\n")

outfile.close()