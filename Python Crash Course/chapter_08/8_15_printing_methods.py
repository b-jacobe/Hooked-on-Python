"""
8_15_printing_methods.py

Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.

Created: 2-14-19
@author: Brian Jacobe

"""

import printing_functions

user_incomplete_items = ['iPod', 'Tabla', 'KH3 Statue', 'FF7 Statue']
user_completed_items = []

user_model = printing_functions.print_models(user_incomplete_items, user_completed_items)
print(user_model)

print(printing_functions.show_completed_models(user_completed_items))