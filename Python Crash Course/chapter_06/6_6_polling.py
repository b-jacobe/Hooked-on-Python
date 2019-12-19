"""
6_6_polling.py

Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

Created: 1-26-19
@author: Brian Jacobe

"""

favorite_languages = {
	'Brian': "Python",
	'Sophia': "Java",
	'Sasha': "Shell"
}

friend_poll = ["Steve", "Kim", "Ben", "Khia", "Brian"]

for name in friend_poll:
	if name in favorite_languages:
		print(name.title() + ", thank you for taking the poll!")
	else:
		print(name.title() + ", you're invited to take the favorite language poll!")
