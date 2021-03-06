"""
9_3_users.py

Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.

Created: 2-26-19
Updated: 12-30-19
@author: Brian Jacobe

"""

class User():
	"""User profile class creation"""

	def __init__(self, first_name, last_name, age, salary, height, weight):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.salary = salary
		self.height = height
		self.weight = weight

	def describe_user(self):
		description = "Here are some fun facts about the you: " + "\n" +
			"Age: " + str(self.age) + "\n" +
			"Salary: " + str(self.salary) + "\n" +
			"Height: " + self.height + "\n" +
			"Weight: " + str(self.weight) + " lbs."
		return description

	def greet_user(self):
		greetings = "Hello, " + self.first_name.title() + " " + self.last_name.title() + "!"
		return greetings

new_user = User("Brian", "Jacobe", 27, 120000, "5'6", 156)
print(new_user.greet_user())
print(new_user.describe_user())
