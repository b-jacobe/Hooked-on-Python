"""
10_5_programming_poll.py

Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.

Created: 4-3-19
Last Updated:
@author: Brian Jacobe

"""

prompt = "Why do you enjoy programming?\n"

filename = "programming_reasons.txt"
user_input = ""

while user_input != "q":
	user_input = input(prompt)
	with open(filename, 'a') as file_object:
		file_object.write(user_input)
		file_object.close()