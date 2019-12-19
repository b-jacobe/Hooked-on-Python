"""
10_4_guest_book.py

Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.

Created: 4-3-19
Last Updated:
@author: Brian Jacobe

"""

prompt = "Please enter your name here.\n"
prompt += "Press Q to quit the program."
filename = "guest_book.txt"
user_input = ""

while user_input != "q":
	user_input = input(prompt)
	with open(filename, 'a') as file_object:
		file_object.write("Welcome, " + user_input + "!")
		file_object.close()