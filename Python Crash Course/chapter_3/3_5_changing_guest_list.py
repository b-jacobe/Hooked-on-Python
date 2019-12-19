"""
3_5_changing_guest_list.py

You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""
invitation_message = ", please join me for dinner and drinks."
guest_list = ['Bruce Lee', 'Theodore Roosevelt', 'Chester Bennington']
print(guest_list[0] + " can't make it to dinner.")
del guest_list[0]
guest_list.insert(0, 'Khia Bautista')

for i in guest_list:
	print("Hi " + i + invitation_message)