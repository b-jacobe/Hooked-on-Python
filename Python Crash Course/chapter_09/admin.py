"""
admin.py

Stores the Privileges and Admin classes
into a seperate module.

Created: 3-13-19
@author: Brian Jacobe
"""

from user import User

class Privileges():
	def __init__(self):
		"""Initialize class that stores a list of priviledges"""
		self.privileges = ["read", "delete", "modify", "block"]

	def show_privileges(self):
		message = "Admin has the following permissions: "
		print(message)
		for actions in self.privileges:
			print(actions)
		return ""


class Admin(User):
	def __init__(self, first_name, last_name, age, salary, height, weight):
		super().__init__(first_name, last_name, age, salary, height, weight)
		self.privileges = Privileges()
