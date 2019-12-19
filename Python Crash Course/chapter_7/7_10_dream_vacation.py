"""
7_10_dream_vacation.py

Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.

Created: 2-5-19
@author: Brian Jacobe

"""

dream_poll = {}
poll_active = True

while poll_active:
	name = input("What is your name? ")
	vacation = input("where is your dream vacation? ")
	dream_poll[name] = vacation
	repeat = input("Would you like to ask another person their dream vacation? (yes/no) ")
	if repeat == "no":
		poll_active = False
print("\n----- Poll Results ------")
for name, vacation in dream_poll.items():
	print(name + "'s prefered dream vacation spot is: " + vacation)