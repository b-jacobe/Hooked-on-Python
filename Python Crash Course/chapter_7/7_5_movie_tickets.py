"""
7_5_movie_tickets.py

A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.

Created: 2-3-19
@author: Brian Jacobe

"""

amc_message = "\nWelcome to AMC theaters, please enter the customer's age."
amc_message += "\na ticket price will display showing the appropriate cost."
amc_message += "\nEnter 'quit' to exit."

customer_age = ""

while customer_age != "quit":
	customer_age = input(amc_message)
	if int(customer_age) < 3:
		print("Your ticket is free!")
	elif int(customer_age) > 3 and int(customer_age) < 12:
		print("Your ticket is $10")
	elif int(customer_age) > 15:
		print("Your ticket is $15")
