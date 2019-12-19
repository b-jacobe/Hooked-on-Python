"""
7_2_restaurant_seating.py

Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.

Created: 1-29-19
@author: Brian Jacobe

"""

head_count = input("How many people are in your party? ")
head_count = int(head_count)
if head_count > 8:
	print("Sorry, you will have to wait for a table.")
else:
	print("Your table is ready.")