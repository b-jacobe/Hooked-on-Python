"""
7_3_multiples_of_ten.py

Ask the user for a number, and then report whether the
number is a multiple of 10 or not.

Created: 1-29-19
@author: Brian Jacobe

"""

user_input = input("Please enter a number: ")
user_input = int(user_input)
if user_input % 10 == 0:
	print("This value is a multiple of ten!")
else:
	print("This value is not a multiple of ten.")