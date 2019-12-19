"""
3_2_greetings.py

Start with the list you used in Excercise 3-1, but instead
of just printing each name, print a message to them. The
text of each message should be the same, but each message
should be personalized with the person's name

BONUS: Added for loop to clean the code

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

names = ['Brian', 'Khia', 'Adam', 'Emily', 'Aygun', 'Deborah', 'Jonathan']

message = "Hey there, how's your day "

for i in names:
	print(message + i + "?")

"""
print(message + names[0] + "?")
print(message + names[1] + "?")
print(message + names[2] + "?")
print(message + names[3] + "?")
print(message + names[4] + "?")
print(message + names[5] + "?")
print(message + names[6] + "?")
"""