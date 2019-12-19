"""
9_7_admin.py

An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.

Created: 3-7-19
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

class Admin(User):
	def __init__(self, first_name, last_name, age, salary, height, weight):
		super().__init__(first_name, last_name, age, salary, height, weight)
		self.privileges = ["read", "delete", "modify", "block"]

	def show_privileges(self):
		message = "Admin has the following permissions: "
		print(message)
		for actions in self.privileges:
			print(actions)
		return ""

riot_admin = Admin("Brian","Jacobe", 27, 120000, "5'6", 155)
print(riot_admin.show_privileges())
