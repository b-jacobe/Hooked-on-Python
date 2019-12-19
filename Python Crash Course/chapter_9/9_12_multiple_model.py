"""
9_12_multiple_modles.py

Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.

Created: 3-13-19
@author: Brian Jacobe
"""

from user import User
from admin import Privileges, Admin

my_admin = Admin("Brian", "Jacobe", 27, 120000, "5'6", 150)
my_admin.privileges.show_privileges()