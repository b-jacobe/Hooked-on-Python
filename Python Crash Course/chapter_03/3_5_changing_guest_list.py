
invitation_message = ", please join me for dinner and drinks."
guest_list = ['Bruce Lee', 'Theodore Roosevelt', 'Chester Bennington']
print(guest_list[0] + " can't make it to dinner.")
del guest_list[0]
guest_list.insert(0, 'Khia Bautista')

for i in guest_list:
	print("Hi " + i + invitation_message)