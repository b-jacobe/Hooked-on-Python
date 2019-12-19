"""
pi_birthday_checker.py

Check to see if my birthday is
in pi.

Created: 3-26-19
@author: Brian Jacobe
"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.rstrip()

#birthday = input("Enter your birthday, in the form mmddyy: ")
birthday = "041791"
if birthday in pi_string:
	print("Your birthday is in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million of pi.")
