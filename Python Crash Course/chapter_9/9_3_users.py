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
		print("Here are some fun facts about the you: ")
		print("Age: " + str(self.age))
		print("Salary: " + str(self.salary))
		print("Height: " + self.height)
		print("Weight: " + str(self.weight) + "lbs.")
		return ""

	def greet_user(self):
		print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")
		return ""

new_user = User("Brian", "Jacobe", 27, 120000, "5'6", 156)
print(new_user.greet_user())
print(new_user.describe_user())
