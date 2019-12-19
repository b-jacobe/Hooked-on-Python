"""
10_3_guest.py

Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.

Created: 3-27-19
@author: Brian Jacobe
"""

filename = "guest.txt"
prompt = "Please enter your name here."
user_input = input(prompt)

if user_input != "":
	with open(filename) as file_object:
		file_object.write(user_input)
		file_object.close()
