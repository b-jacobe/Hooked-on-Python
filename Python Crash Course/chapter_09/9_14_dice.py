"""
9_14_dice.py

Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.

Created: 3-22-19
@author: Brian Jacobe
"""

from random import randint

class Dice():
	"""Simple dice that rolls a number between 1-6"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self, sides):
		die = randint(1,sides)
		return die

sides = 6
my_dice = Dice(sides)
print(str(sides) + "-sided die created.")
print("It's time to roll...")
for i in range(1, 7):
	print(my_dice.roll_die(sides))

sides = 10
my_dice = Dice(sides)
print(str(sides) + "-sided die created.")
print("It's time to roll...")
for i in range(1, 11):
	print(my_dice.roll_die(sides))

sides = 20
my_dice = Dice(sides)
print(str(sides) + "-sided die created.")
print("It's time to roll...")
for i in range(1, 11):
	print(my_dice.roll_die(sides))
