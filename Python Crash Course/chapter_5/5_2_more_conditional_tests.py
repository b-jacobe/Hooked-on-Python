"""
5_2_conditional_tests.py

You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list

Created: 1-18-19
@author: Brian Jacobe

"""
my_goals = ['Work for Riot Games', 'Move to LA', 'Buy a new VW GTI 2019', 'Visit Japan', 'Buy a new phone']

goals_achieved = False
if goals_achieved == True:
	print("Congratulations, you've achieved your goals in 2019. Now go make more!")
else:
	print("You're on your way! Don't give up!")

if 'Meet someone new' in my_goals:
	print('Maybe you should save that goal for later.')
else:
	print('You have a solid list of goals!')

my_goals[0] = 'WORK FOR RIOT GAMES'

if 'WORK FOR RIOT GAMES' in my_goals:
	print('Pass')
else:
	print('Fail')

my_goals[0] = my_goals[0].lower()

if 'work for riot games' in my_goals:
	print('Pass')
else:
	print('Fail')

value = 2

print(value > 1 and value < 3)
print(value < 5 or value > 1)
print(value <= 1)
print(value >= 2)