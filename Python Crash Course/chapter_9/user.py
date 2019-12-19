"""
user.py

Stores the User classes
into a seperate module.

Created: 3-13-19
@author: Brian Jacobe
"""

class User():
	def __init__(self, first_name, last_name, age, salary, height, weight):
		"""Initialize user class attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.salary = salary
		self.height = height
		self.weight = weight
		self.login_attempts = 0

	def describe_user(self):
		"""Display information of user class attributes"""
		print("Here are some fun facts about the you: ")
		print("Age: " + str(self.age))
		print("Salary: " + str(self.salary))
		print("Height: " + self.height)
		print("Weight: " + str(self.weight) + "lbs.")
		return ""

	def greet_user(self):
		"""Return greeting for user"""
		message = "Hello, " + self.first_name.title() + " " + self.last_name.title() + "!"
		return message

	def increment_login_attempts(self):
		"""Increment login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts"""
		self.login_attempts = 0
