"""
6_7_people.py

Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.

Created: 1-28-19
@author: Brian Jacobe

"""
user_1 = {
	"user_name":"Brian Jacobe",
	"family": "yes",
	"family_role":"Father",
	"occupation":"Engineering Manager",
	"salary":180000,
	"pets":"yes"
	}
user_2 = {
	"user_name":"Khia Jacobe",
	"family": "yes",
	"family_role":"Mother",
	"occupation": "Teacher",
	"salary":75000,
	"pets":"yes"
}
user_3 = {
	"user_name":"Maxine Jacobe",
	"family": "yes",
	"family_role": "Daughter",
	"occupation": "Student",
	"salary":0,
	"pets":"yes"
}

people = [user_1, user_2, user_3]

print("Jacobe Family:")
for user in people:
	if user["user_name"] == "Brian Jacobe":
		print("Name: " + user["user_name"])
		print("Family Role: " + user["family_role"])
		print("Occupation: " + user["occupation"])
		print("Salary: " + str(user["salary"]))
		print("Pets: " + user["pets"] + "\n")
	elif user["user_name"] == "Khia Jacobe":
		print("Name: " + user["user_name"])
		print("Family Role: " + user["family_role"])
		print("Occupation: " + user["occupation"])
		print("Salary: " + str(user["salary"]))
		print("Pets: " + user["pets"]+ "\n")
	elif user["user_name"] == "Maxine Jacobe":
		print("Name: " + user["user_name"])
		print("Family Role: " + user["family_role"])
		print("Occupation: " + user["occupation"])
		print("Salary: " + str(user["salary"]))
		print("Pets: " + user["pets"]+ "\n")