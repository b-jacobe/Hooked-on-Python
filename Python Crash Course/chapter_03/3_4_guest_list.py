"""
3_4_guest_list.py

If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

guest_list = ['Bruce Lee', 'Theodore Roosevelt', 'Chester Bennington']
invitation_message = ", I would like to invite you to dinner."

for i in guest_list:
	print("Hi " + i + invitation_message)