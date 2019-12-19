"""
3_6_more_guest.py

You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

guest_list = ['Khalil Saado', 'Adam Rao', 'Aygun Vera']
invitation_message = ", please join me for dinner and drinks tomorrow @ 7PM"
ending_message = "I found a bigger dinner table."

print(guest_list[0] + " can't make it to dinner.")

del guest_list[0]
guest_list.insert(0, 'Khia Bautista')
guest_list.insert(0, 'Deborah Galvan')
guest_list.insert(1, 'Jonathan DeSimone')
guest_list.append('Sean Rubin')

for i in guest_list:
	print("Hi " + i + invitation_message)

print(ending_message)
		

