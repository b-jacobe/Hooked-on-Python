"""
9_11_imported_admin.py

Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.

Created: 3-13-19
@author: Brian Jacobe
"""

from admin import User, Privileges, Admin

my_admin = Admin("Brian", "Jacobe", "27", 120000, "5'6",150)
my_admin.privileges.show_privileges()