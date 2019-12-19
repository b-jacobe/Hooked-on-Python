"""
6_10_favorite_numbers.py

Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.

Created: 1-28-19
@author: Brian Jacobe

"""

user_info = {
	"Brian":[1,28,30,40,50],
	"Jonathan":117,
	"Aygun":[21,50],
	"Khia":[0,1,24],
	"Deborah":17
	}

# Sorted function to get a copy of key-values in order
for name, number in sorted(user_info.items()):
	print("\nUser: " + name)
	print("Favorite Number: " + str(number) + "\n")
 