"""
5_9_no_users.py

Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.

Created: 1-20-19
@author: Brian Jacobe

"""

usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

for i in usernames:
	if i == 'admin':
		print('Hello ' + i + ", would you like to see a status report?")
	else:
		print('Hello ' + i + ", thank you for logging in again.")

del usernames[:]

#PYTHONIC
if not usernames:
	print("List is empty. - Method 1")

if usernames == []:
	print("List is empty. - Method 2")