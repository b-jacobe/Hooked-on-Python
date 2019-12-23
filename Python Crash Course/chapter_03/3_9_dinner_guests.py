guest_list = ['Bruce Lee', 'Theodore Roosevelt', 'Chester Bennington']
invitation_message = ", I would like to invite you to dinner."

for i in guest_list:
	print("Hi " + i + invitation_message)

print("I have invited: " + str(len(guest_list)) + " people for dinner.")