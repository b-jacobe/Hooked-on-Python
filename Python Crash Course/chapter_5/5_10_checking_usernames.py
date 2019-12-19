"""
5_10_checking_usernames.py

Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.

Created: 1-20-19
@author: Brian Jacobe

"""
"""
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
"""
c_users = ["bjacobe", "admin"]
n_users = ["BJACOBE", "jsmith"]

n_users = [j.lower() for j in n_users]
c_users = [k.lower() for k in c_users]

for i in n_users:
	if i in c_users:
		print("user already exists.")
	else:
		print("added.")
