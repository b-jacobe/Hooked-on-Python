"""
7_6_three_exits.py

Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.

Created: 2-3-19
@author: Brian Jacobe

"""

amc_message = "\nWelcome to AMC theaters, please enter the customer's age."
amc_message += "\na ticket price will display showing the appropriate cost."
amc_message += "\nEnter 'quit' to exit."

customer_age = ""

while true:
	customer_age = input(amc_message)
	if int(customer_age) < 3:
		print("Your ticket is free!")
	elif int(customer_age) > 3 and int(customer_age) < 12:
		print("Your ticket is $10")
	elif int(customer_age) > 15:
		print("Your ticket is $15")
	elif customer_age == "quit"
		break