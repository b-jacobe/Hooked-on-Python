"""
3_3_your_own_list.py

Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”

BONUS: Added for loop to clean the code

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""
personal_vehicles = ['Audi S4', 'Ducati Sport 1000', 'Audi Q7S']
goal_message = "My future cars are: "

print (goal_message)

for i in personal_vehicles:
	print (i)
	if i == 'Audit Q7S':
		break

personal_vehicles.append('VW GTI R')
print(personal_vehicles)
