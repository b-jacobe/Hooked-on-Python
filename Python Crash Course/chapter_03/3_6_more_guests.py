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
		

