"""
4_12_more_loops.py

All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

Created: 1-15-19
Last Updated: 
@author: Brian Jacobe

"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
#print(my_foods)

for i in my_foods:
	print(i)

print("\nMy friend's favorite foods are:")
#print(friend_foods)

for j in friend_foods:
	print(j)