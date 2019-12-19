"""
9_4_number_served.py

Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.

Created: 3-2-19
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

new_user = User("Brian","Jacobe", 27, 120000,"5'6", 150)
print(new_user.greet_user())
print("Login attempts: " + str(new_user.login_attempts))
print("Now attempting to login...")
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print("Login attempts: " + str(new_user.login_attempts))
print("Now reseting login count...")
new_user.reset_login_attempts()
print("Login attempts: " + str(new_user.login_attempts))

