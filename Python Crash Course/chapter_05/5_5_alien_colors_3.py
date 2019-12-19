"""
5_5_alien_colors_3.py

Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.

Created: 1-19-19
@author: Brian Jacobe

"""

alien_color = ['green', 'red', 'yellow']
for i in alien_color:
	if i == 'green':
		print('+5 points')
	elif i == 'yellow':
		print('+10 points')
	elif i == 'red':
		print('+15 points')

