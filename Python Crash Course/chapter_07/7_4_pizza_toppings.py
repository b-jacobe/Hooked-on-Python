"""
7_4_pizza_toppings.py

Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.

Created: 2-3-19
@author: Brian Jacobe

"""

dominos_welcome = "\nWelcome to Dominos! Please select your toppings for your pizza."
dominos_welcome += "\nEnter 'quit' to exit the program."
user_order = ""

while user_order != "quit":
	user_order = input(dominos_welcome)
	print(user_order)
