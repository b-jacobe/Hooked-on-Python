"""
5_4_alien_colors_2.py

Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.

Created: 1-19-19
@author: Brian Jacobe

"""

alien_color = 'red'
alien_color = 'green'

if alien_color == 'green':
	print('+5 points')
else:
	print('+10 points')
