"""
6_1_person.py

Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
6-2. Favorite Numbers: Use a dictionary to store

Created: 1-24-19
@author: Brian Jacobe

"""

user_info = {
	"user_name":"bjacobe",
	"salary":120000,
	"dogs":"yes"
	}

print(user_info["user_name"])

print(user_info["salary"])

print(user_info["dogs"])


user_info["vehicles"] = 3

print(user_info["vehicles"])