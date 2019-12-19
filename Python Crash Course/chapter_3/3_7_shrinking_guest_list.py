"""
3_7_shrinking_guest_list.py

Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""
guest_list = ['Khalil Saado', 'Adam Rao', 'Aygun Vera']
invitation_message = ", please join me for dinner and drinks tomorrow @ 7PM"
ending_message = "I found a bigger dinner table."
apology_all_message = "Hi all, unfortunately, I can only invite 2 people."
apology_message = " sorry, we can't fit everyone. Let's hangout some other time!"

print(guest_list[0] + " can't make it to dinner.")

del guest_list[0]
guest_list.insert(0, 'Khia Bautista')
guest_list.insert(0, 'Deborah Galvan')
guest_list.insert(2, 'Jonathan DeSimone')
guest_list.append('Sean Rubin')

for i in guest_list:
	print("Hi " + i + invitation_message)

print(ending_message + "\n")
print(apology_all_message)

for i in reversed(guest_list):
	if i == "Khia Bautista":
		break
	else:
		print(i + apology_message)
		guest_list.pop()


for i in guest_list:
	print("Hi " + i + ", you're still invited for dinner and drinks!")

del guest_list[0]
del guest_list[0]

print(guest_list)

