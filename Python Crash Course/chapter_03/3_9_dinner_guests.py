"""
3_9_dinner_guests.py

Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

guest_list = ['Bruce Lee', 'Theodore Roosevelt', 'Chester Bennington']
invitation_message = ", I would like to invite you to dinner."

for i in guest_list:
	print("Hi " + i + invitation_message)

print("I have invited: " + str(len(guest_list)) + " people for dinner.")