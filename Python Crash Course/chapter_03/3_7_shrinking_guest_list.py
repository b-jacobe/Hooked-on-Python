
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

